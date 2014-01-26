Title: Process-Based Job Management in C and Python
Date: 2012-02-20 15:56
Category: all
Tags: C, python
Slug: process-based-job-management-in-c-and-python

I had an interesting discussion with my buddy Ali after he read my
previous post, [Python Multiprocessing Pool and KeyboardInterrupt
Revisited][]. The discussion was around the question, "what are the
benefits of using the python [multiprocessing.Pool][] class over writing
a simple process-based job management system in C?"

We started with a discussion of performance. It’s no secret that C will
outperform python in any task; after all python is an interpreted
language and the standard python implementation is written in C.
However, Ali and my discussion was not focused on the performance of the
jobs themselves, but rather on the performance of a job management
system that could be gracefully interrupted. In such a system, where the
majority of work is done in job processing, the question of the job
management system's performance is irrelevant; it makes little
difference if C can launch all the workers thirty times faster when
python still does it in well under a second. As an aside, it's trivial
to call a C program from python, or even to write a [python C module][]
for fast job processing performance.

Once the irrelevance of the job management performance was agreed upon,
Ali and I discussed development time, dependencies and portability.
Having written both a significant amount of C and python code pertaining
to [operating system concepts][], I know that anyone with equivalent
experience can much more efficiently code a process-based job management
system in python than in C. This holds true, even without the
multiprocessing module and when using only the low level features
provided by the [os package][]. The two primary reasons for faster
development time are dynamic types, and garbage collection.
Additionally, python provides a lot more out-of-the-box functionality,
e.g., string manipulation and basic data structures such as lists and
dictionaries; all features that contribute to faster development time.

Of course, if one had all the needed libraries in C, then my only
argument in favor of python is the lack of types and implicit memory
management. The choice between C and python in this case is simply up to
personal preference. However, having the required C libraries is a
problem on its own. This is where my lack of real-world C experience
appears as I’m not familiar with well-written C libraries that provide
python-like string manipulation and basic data structures, nor am I
familiar with a well written process-based job management library.
Nevertheless, even if these libraries were easily available, they are
additional dependencies that must be present in order to run any code
utilizing them.

Managing dependencies can be a pain, especially in the absence of an
automated process for obtaining them. For example, I wrote some code for
a computer graphics class a few years ago that I recently wanted to
compile. As I recall, it took me a few hours to find and install all the
required OpenGL dependencies before I could compile my own code. Compare
that to the 90%+ of python programs I’ve written which have no external
dependencies. This vast amount of code *still* works out-of-the-box
across multiple platforms.

Portability is my final argument in favor of python over C. While
[ANSI-C][] based libraries should work across multiple platforms,
dealing with process management is a whole other can of worms as this
*drastically* differs between operating systems. Again, my inexperience
shows as I am not familiar with any process management libraries that
are compatible with both Windows and [POSIX-based][] systems. Moreover,
I am not even sufficiently familiar with the Windows API to know its
equivalent functions to [fork][], [exec][], [pipe][] and [dup][] that
are needed to write a process-based job management system for Windows.
Nevertheless, with python, one needn’t worry about such things because
the majority of the functionality in the os package is supported on both
Windows and POSIX-based systems. Most importantly the multiprocessing
module is supported on both, and thus *anyone* who installs python,
independent of their operating system, can run the multiprocessing
examples I previously provided [[1][], [2][]].

While Ali and I had a great discussion going, we still hadn’t gotten to
the root of his question. Ali didn’t care about development time, nor
portability. The problem was that he didn’t see any significant
advantages to using the multiprocessing.Pool class when he could instead
quickly write a process-based job management system in C utilizing fork
to spawn processes and pipe to handle the [inter-process
communication][] (IPC). As it turns out, Ali wasn’t aware that the
python multiprocessing.Pool class internally handles all the IPC.
Without the built-in IPC support, Ali’s concerns would be valid as some
other communication mechanism would need to be explicitly written to
communicate between the master process and its workers. Fortunately, in
python we get all that for free with both the multiprocessing.Pool and
[multiprocessing.Queue][] classes.

Personally, the choice of using python for such a task is a no-brainer
because I can develop the system faster without the need for external
dependencies and have confidence that it will work on any operating
system that python runs on. Nevertheless, my curiosity peaked and I set
out to write a *simple* process-based job management system in C. The
system is complete, ~~though I've yet to write about
it~~<ins datetime="2012-02-24T07:02:59+00:00"> and I've now written
about it. Read the followup: [Implementation of a Process-Based Job
Management System in C][]</ins>

  [Python Multiprocessing Pool and KeyboardInterrupt Revisited]: /2012/02/14/python-multiprocessing-pool-and-keyboardinterrupt-revisited/
  [multiprocessing.Pool]: http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
  [python C module]: /2010/09/14/properly-handling-the-keyboard-interrupt-exception-sigint-within-a-python-c-module/
    "Properly Handling the Keyboard Interrupt Exception (SIGINT) within a Python C Module"
  [operating system concepts]: http://cs.ucsb.edu/~bboe/p/cv#teaching
  [os package]: http://docs.python.org/library/os.html
  [ANSI-C]: http://en.wikipedia.org/wiki/ANSI_C
  [POSIX-based]: http://en.wikipedia.org/wiki/POSIX
  [fork]: http://pubs.opengroup.org/onlinepubs/009604599/functions/fork.html
  [exec]: http://pubs.opengroup.org/onlinepubs/009604499/functions/exec.html
  [pipe]: http://pubs.opengroup.org/onlinepubs/009604599/functions/pipe.html
  [dup]: http://pubs.opengroup.org/onlinepubs/007904975/functions/dup.html
  [1]: /2010/08/26/python-multiprocessing-and-keyboardinterrupt/
    "Python Multiprocessing and KeyboardInterrupt"
  [2]: /2011/01/28/the-python-multiprocessing-queue-and-large-objects/
    "The Python Multiprocessing Queue and Large Objects"
  [inter-process communication]: http://en.wikipedia.org/wiki/Inter-process_communication
  [multiprocessing.Queue]: http://docs.python.org/library/multiprocessing.html#exchanging-objects-between-processes
  [Implementation of a Process-Based Job Management System in C]: /2012/02/23/implementation-of-a-process-based-job-management-system-in-c/
    "Implementation of a Process-Based Job Management System in C"
