Title: Implementation of a Process-Based Job Management System in C
Date: 2012-02-23 23:03
Category: all
Tags: C, python
Slug: implementation-of-a-process-based-job-management-system-in-c

A few days ago I wrote about [a few differences between using C and
python to handle a process-based job management system][]. My discussion
covered performance, development time, dependencies, and portability. I
ended with the conclusion that despite C being vastly superior in
performance, the relative difference in performance between various job
management systems is irrelevant when considering the job processing
time. Therefore, I recommended using python for such a task due to
faster development times, built-in support for multiprocessing (no need
for third-party libraries), and the portability one immediately gains by
using python.

In spite of my continuing recommendation to use python for such a task,
I was curious what a C solution might look like. Thus, I set out to
write, and did write, a simple process-based job management system in C
that offers similar functionality as python's [multiprocessing.Pool][]
class. Take note that writing this system required more time than the
equivalent python code would have, however, the point is moot because
python has the multiprocessing.Pool class. Furthermore, whoever wants to
use this system must manually include it in their project, thus
introducing a third-party dependency in their code. Finally, this code
will not compile in the typical Windows development environment as it
relies on [POSIX-based][] system calls. Hence, for all the reasons I
previously mentioned, this C implementation is quite inferior to
python's multiprocessing.Pool class.

The source that I reference throughout the remainder of this post can be
[found and downloaded in entirety][]. On a POSIX-based machine the code
can be compiled via `gcc main.c job_management.c`{.inline} and the test
program can be run via `./a.out`{.inline}.

The system, or library, is contained in two files: **job\_management.h**
and **job\_management.c**. Anyone familiar with C or C++ development
knows that **job\_management.h** is a header file which contains the
structures and function prototypes whereas **job\_management.c**
contains the implementation. The entire library functionality is exposed
through three functions: `manager_init`{.inline},
`manager_run_jobs`{.inline}, and `manager_destruct`{.inline}.

~~~~ {lang="c"}
void manager_init(struct manager *manager, int num_workers,
          void (*input_callback)(char *),
          void (*output_callback)(char *),
          void (*work_function)(char *));
~~~~

Aside from the pre-allocated *manager* structure that all the functions
require as their first parameter, the `manager_init`{.inline} function
requires four other parameters: *num\_workers*, *input\_callback*,
*output\_callback*, and *work\_function*. The *num\_workers* parameter
specifies an upper bound on how many worker processes to start. Each of
the remaining parameters are function pointers to functions that must
each have a single char pointer parameter and return no value. I will
describe the purpose of these functions in the order that they execute
when considering only a single job.

The *input\_callback* function is called by the master process, once per
job, in order to fetch the input for the job. The callback function
stores the job input in the provided buffer before returning. The
*work\_function* function is the reason for the entire system as this
function performs the job processing. In this function, the provided
buffer serves both as job input and job output. On invocation, the
buffer contains the result of a prior call to *input\_callback* which
has been sent over a pipe between the master process and worker process.
On return, the buffer should contain the job output which will then be
sent back to the master process. The *output\_callback* function is
called by the master process as each job is completed. In this case, the
buffer contains the output of a completed job.

~~~~ {lang="c"}
int manager_run_jobs(struct manager *manager, int num_jobs);
~~~~

Once the manager has been properly set up, a number of jobs can be
started via `manager_run_jobs`{.inline} which takes one additional
argument, *num\_jobs*. Intuitively this parameter represents the number
of jobs to process. This function contains the most complicated piece of
the system as it is responsible for forking the processes, setting up
the pipes between the master and workers, cleaning up the address space
and file descriptor table for the workers, and properly using I/O
multiplexing in order to both send job input and receive job output.

One additional complication that the `manger_run_jobs`{.inline} function
has to handle is [the issue][] that started this entire series of blog
posts; that is, the want to gracefully exit the job management system
when a keyboard interrupt (SIGINT), occurs. Gracefully exiting means any
jobs that are running at the time of the keyboard interrupt will
successfully complete prior to exiting, thus giving the master process
the chance to save partial results. This function handles the desired
behavior through the combination of a global [volatile][] value that's
periodically checked within this function's primary loop, and a SIGINT
handler function that updates the value. Worker processes are unaffected
by SIGINT as they are set to ignore it.

~~~~ {lang="c"}
void manager_destruct(struct manager *manager);
~~~~

The last function, `manager_destruct`{.inline}, conveniently frees the
contents of the *manager* structure. It is important to note that this
function is also called by each worker as part of its address space and
file descriptor table clean up. For this reason, the
`manager_destruct`{.inline} function handles the closing of some *FILE*
structures. Otherwise, this function is incredibly simple.

As previously mentioned, my job\_management library is simple and thus
is no where near as flexible as python's multiprocessing.Pool class.
Furthermore, my library has no support for data serialization as it
relies on messages being no larger than *MAX\_MESSAGE* bytes in size,
and has a limitation that the message contents span only a single line.
These restrictions were chosen for simplicity and are, by no means, a
limitation of C. However, again, I must point out that object
serialization is provided by default with python, and is built into the
multiprocess.Pool class.

Below is an example program that demonstrates using my process-based job
management system. Note that this code really isn't that complicated,
especially when compared to [the python solution that gracefully handles
the keyboard interrupt][]. Of course, the python solution is without
dependencies and much more portable. :)

Happy coding!

[gist id=1894848 file=main.c]

  [a few differences between using C and python to handle a
  process-based job management system]: http://www.bryceboe.com/2012/02/20/process-based-job-management-in-c-and-python/
    "Process-Based Job Management in C and Python"
  [multiprocessing.Pool]: http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
  [POSIX-based]: http://en.wikipedia.org/wiki/POSIX
  [found and downloaded in entirety]: https://gist.github.com/1894848
  [the issue]: http://www.bryceboe.com/2010/08/26/python-multiprocessing-and-keyboardinterrupt/
    "Python Multiprocessing and KeyboardInterrupt"
  [volatile]: http://en.wikipedia.org/wiki/Volatile_variable
  [the python solution that gracefully handles the keyboard interrupt]: http://www.bryceboe.com/2012/02/14/python-multiprocessing-pool-and-keyboardinterrupt-revisited/
    "Python Multiprocessing Pool and KeyboardInterrupt Revisited"
