Title: Python Multiprocessing and KeyboardInterrupt
Date: 2010-08-26 01:28
Category: all
Tags: python
Slug: python-multiprocessing-and-keyboardinterrupt

<ins datetime="2012-02-14T21:55:40+00:00">
Update 2012/02/14: Added post: [Python Multiprocessing Pool and
KeyboardInterrupt Revisited][]</ins>

<ins datetime="2011-02-03T17:43:45+00:00">
Update 2011/02/03: [Added commentary][] regarding Georges's comment about [this
stackoverflow thread][].</ins>

<ins datetime="2011-01-28T18:58:40+00:00">
Update 2011/01/28: There is an issue with this code when passing large objects
through the queue. While the code listed below will work in most situations,
consider using sentinels to indicate the end of jobs in your queue rather than
relying on the Queue.Empty error. You can read about that in my post titled,
[The Python Multiprocessing Queue and Large Objects][].</ins>

I was recently working on improving the efficiency of my botnet analysis code
by utilizing 100% of the CPU resources available to my machine. In order to do
that in python I needed to span multiple processes as multithreading would
produce no benefit for these CPU bound events. While python utilizes true
threads that have the ability to run on different cores concurrently, the
Global Interpreter Lock, or GIL, makes it such that only one of these threads
can run "concurrently". Thus the simplest solution seemed to be utilizing
python's [multiprocessing][] module.

Python's multiprocessing module is actually quite simple to use, especially if
you've previously used python's [threading][] module. Additionally the
multiprocessing module contains a pool class which automatically sets up
processes to manage a pool of jobs. There is, however, one *HUGE* caveat. The
pool of workers cannot be terminated until all the tasks have been consumed.
After some simple experimentation I noticed two key things with the
**multiprocessing.pool** feature. First, while the worker processes can handle
the **KeyboardInterrupt** and call **sys.exit**, these processes persist and
thus receive future tasks. Second, the **KeyboardInterrupt** is not delivered
to the parent process until all jobs are completed.

    #!/usr/bin/env python
    import multiprocessing, os, time

    def do_work():
        print 'Work Started: %d' % os.getpid()
        time.sleep(2)
        return 'Success'

    def pool_function():
        try:
            return do_work()
        except KeyboardInterrupt:
            return 'KeyboardException'

    def main():
        pool = multiprocessing.Pool(3)
        try:
            jobs = []
            for i in range(6):
                jobs.append(pool.apply_async(pool_function, args=()))
            pool.close()
            pool.join()
        except KeyboardInterrupt:
            print 'parent received control-c'
            pool.terminate()

        for i in jobs:
            if i.successful():
                print i.get()
            else:
                print 'Job failed: %s %s' % (type(i._value), i._value)

    if __name__ == "__main__":
        main()

I constructed a fairly simple example of this behavior, shown above. Running
the code will span three worker processes to handle a total of six jobs. The
job is very simple: display a message, sleep for two seconds and return a
message to the parent. You'll notice that when you send a **KeyboardInterrupt**
by pressing ctrl+c (on Linux) it'll kill the currently running child processes,
however the next job will simply take its place until there are no remaining
jobs.

    #!/usr/bin/env python
    import multiprocessing, os, signal, time, Queue

    def do_work():
        print 'Work Started: %d' % os.getpid()
        time.sleep(2)
        return 'Success'

    def manual_function(job_queue, result_queue):
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        while not job_queue.empty():
            try:
                job = job_queue.get(block=False)
                result_queue.put(do_work())
            except Queue.Empty:
                pass
            #except KeyboardInterrupt: pass

    def main():
        job_queue = multiprocessing.Queue()
        result_queue = multiprocessing.Queue()

        for i in range(6):
            job_queue.put(None)

        workers = []
        for i in range(3):
            tmp = multiprocessing.Process(target=manual_function,
                                          args=(job_queue, result_queue))
            tmp.start()
            workers.append(tmp)

        try:
            for worker in workers:
                worker.join()
        except KeyboardInterrupt:
            print 'parent received ctrl-c'
            for worker in workers:
                worker.terminate()
                worker.join()

        while not result_queue.empty():
            print result_queue.get(block=False)

    if __name__ == "__main__":
        main()

In order to behave as I would expect it to, I had to stop using the
*convenient* pool feature and thus I wrote the pool handling code myself as
displayed above. By running the code, you'll notice that I had to implement a
**job\_queue** and **result\_queue** to pass information between the parent and
children processes. More importantly you'll notice that when you send a
**KeyboardInterrupt** the remaining tasks are not executed and the parent
safely exits almost immediately. One final note is that I chose to ignore
KeyboardInterrupts in the child completely by using the **signal** module. This
functionality could additionally be accomplished with the except statement
commented out on line 17.

On a separate note, I would like to say that this is my 100th blog post.
Awesome!

<a name="georges"></a>**Response to Georges comment on 2011/02/03**  
In response to Georges comment I wanted to see how such an approach would work
in a case similar to what was done above. The below code demonstrates the
approach from the stackoverflow response by Glenn Maynard to call the get
function with a timeout.

    #!/usr/bin/env python                                                           
    import multiprocessing, os, time

    def do_work(i):
        try:
            print 'Work Started: %d %d' % (os.getpid(), i)
            time.sleep(2)
            return 'Success'
        except KeyboardInterrupt, e:
            pass

    def main():
        pool = multiprocessing.Pool(3)
        p = pool.map_async(do_work, range(6))
        try:
            results = p.get(0xFFFF)
        except KeyboardInterrupt:
            print 'parent received control-c'
            return

        for i in results:
            print i

    if __name__ == "__main__":
        main()

This code works exactly as expected (yay!) however there is one difference
between this approach and my solution. With this approach, as is, it is not
possible to retrieve the results which completed prior to the keyboard
interrupt. If that is not important, than this is a much more elegant solution.
Thanks for bringing the solution to my attention Georges.

  [Python Multiprocessing Pool and KeyboardInterrupt Revisited]: /2012/02/14/python-multiprocessing-pool-and-keyboardinterrupt-revisited/
  [Added commentary]: #georges
  [this stackoverflow thread]: http://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool
  [The Python Multiprocessing Queue and Large Objects]: /2011/01/28/the-python-multiprocessing-queue-and-large-objects/
  [multiprocessing]: http://docs.python.org/library/multiprocessing.html
  [threading]: http://docs.python.org/library/threading.html
