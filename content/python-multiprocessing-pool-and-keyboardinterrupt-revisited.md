Title: Python Multiprocessing Pool and KeyboardInterrupt Revisited
Date: 2012-02-14 13:54
Category: all
Tags: python
Slug: python-multiprocessing-pool-and-keyboardinterrupt-revisited

Earlier today I was in the process of cleaning out some Chrome bookmarks
when I came across a post by John M. Reese I bookmarked titled, [Python:
Using KeyboardInterrupt with a Multiprocessing Pool][]. I had bookmarked
John's post a number of months ago as it referenced my previous post,
[Python Multiprocessing and KeyboardInterrupt][], however, not until
today had I been able to look at his findings.

John suggests that by having the worker processes ignore SIGINT, the
signal that results in python's KeyboardInterrupt, the entire problem
can be solved. Astute readers will note that I actually used the same
approach in my [second update][] to my aforementioned post, which
suffered from the problem that intermediate results could not be
processed, i.e., jobs that completed prior to the keyboard interrupt.
While, John's solution did educate me as to the existence of the
initializer and initargs parameters to the [multiprocessing.Pool][]
function, his solution in-fact does not work. The only reason it appears
to work is due to the `time.sleep(10)`{.inline} in his try block. In
most code this `sleep`{.inline} call would not exist, rather the code
would immediately call `join()`{.inline} on the pool object.

In the absence of the delay introduced by the `sleep`{.inline} call,
John's code still suffers from the original problem which is the
KeyboardInterrupt exception does not reach the main process until all of
the jobs have completed. The proper solution to the problem would be to
fix the multiprocessing library to allow the `join`{.inline} function to
be interrupted. Until then, my suggestion of rolling your own pool
functionality is the best solution I am aware of.

Below is a verbatim copy of my original solution for your convenience:

~~~~ {lang="python" line="1"}
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
~~~~

  [Python: Using KeyboardInterrupt with a Multiprocessing Pool]: http://noswap.com/blog/python-multiprocessing-keyboardinterrupt/
  [Python Multiprocessing and KeyboardInterrupt]: /2010/08/26/python-multiprocessing-and-keyboardinterrupt/
  [second update]: /2010/08/26/python-multiprocessing-and-keyboardinterrupt/#georges
  [multiprocessing.Pool]: http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
