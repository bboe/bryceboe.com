Title: The Python Multiprocessing Queue and Large Objects
Date: 2011-01-28 01:16
Category: all
Tags: python
Slug: the-python-multiprocessing-queue-and-large-objects

The [Usenix security][] deadline is quickly approaching, and that means
finalizing everything on my research project. Therefore, today I *wanted to*
quickly parallelize some of my analysis code to take advantage of the eight
virtual processors on my machine. I previously wrote about [python
multiprocessing and keyboard interrupts][], so the task of converting my code
seemed pretty trivial. Unfortunately, my analysis code deals with large amounts
of data which when passed to processes using the [multiprocessing queue
class][], produced unexpected results. Thus the sample I originally used in my
previous post, isn't as robust as I hoped. <del>It will soon be updated.<del>
<ins datetime="2011-01-28T19:08:44+00:00">The post has been updated with a
reference to this post.</ins>

The issue is that when pushing large items onto the queue, the items are
essentially buffered, despite the immediate return of the queue's *put*
function [endnote [1][]]. Therefore, the queue may have not yet completely
added an item by the time a subsequent non-blocking call to the queue's *get*
function is made. This delay explains why such a non-blocking call to
**queue.get** may return a **Queue.Empty** error and is the exact problem I
encountered in my analysis code.

As usual, I have provided some code demonstrating the problem and a solution.

    #!/usr/bin/env python
    import multiprocessing, Queue

    def worker_bad(jobs):
        while True:
            try:
                tmp = jobs.get(block=False)
            except Queue.Empty:
                break

    def worker_good(jobs):
        while True:
            tmp = jobs.get()
            if tmp == None:
                break

    def main(items, size, num_workers, good_test):
        if good_test:
            func = worker_good
        else:
            func = worker_bad
        jobs = multiprocessing.Queue()
        for i in range(items):
            jobs.put(range(size))
        workers = []
        for i in range(num_workers):
            if good_test:
                jobs.put(None)
            tmp = multiprocessing.Process(target=func, args=(jobs,))
            tmp.start()
            workers.append(tmp)
        for worker in workers:
            worker.join()
        return jobs.empty()

    if __name__ == '__main__':
        workers = 4
        items = workers * 2
        size = 10000

        for good_test in [False, True]:
            passed = 0
            for i in range(100):
                passed += main(items, size, workers, good_test=good_test)
            print '%d%% passed (Good Test: %s)' % (passed, good_test)

This code provides a simple test framework to compare two methods for
completing tasks in a job queue. The actual workers are virtually identical as
they simply continue to pull items off the job queue, until there are no more
jobs. An individual test is considered passed when the number of jobs remaining
after the workers terminate is zero. When running this script, you should
notice that the first group has fewer than 100% of the tests pass, and more
importantly that the second group has a 100% pass rate. If your output shows
the first with a 100% pass rate, try doubling or further increasing the value
of the variable **size** on line 39. Additionally you may notice I/O errors.
These errors likely represent a bug in the multiprocessing queue and further
demonstrate that a call to queue.get immediately after queue.put will not
always succeed.

I arrived at the solution to this problem, in the response to a slightly
similar stackoverflow question titled, [Dumping a multiprocessing.Queue into a
list][]. The solution recommended by the stackoverflow response is to enqueue a
sentinel after all data in order to clearly delineate the end of the queue
rather than utilizing the empty state of the queue. However, a single sentinel
will not work in a case where there are multiple worker processes as only one
worker can receive the sentinel. Thus the intuitive solution is to enqueue as
many sentinels as there are workers on the queue following the data. I chose to
represent these sentinels by the value **None** shown on line 28.

Now I can get back to speeding up my data analysis. Happy coding!

<a name="ref1"></a>Endnote 1: Observant readers might notice that the queue's
put function has a **block** argument, however that argument, **true** by
default, is for cases when the queue has a maximum size.

  [Usenix security]: http://usenix.org/events/sec11/
  [python multiprocessing and keyboard interrupts]: /2010/08/26/python-multiprocessing-and-keyboardinterrupt/
  [multiprocessing queue class]: http://docs.python.org/library/multiprocessing.html#multiprocessing.Queue
  [1]: #ref1
  [Dumping a multiprocessing.Queue into a list]: http://stackoverflow.com/questions/1540822/dumping-a-multiprocessing-queue-into-a-list
