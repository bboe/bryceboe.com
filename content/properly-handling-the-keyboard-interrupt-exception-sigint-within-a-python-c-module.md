Title: Properly Handling the Keyboard Interrupt Exception (SIGINT) within a Python C Module
Date: 2010-09-14 23:54
Category: all
Tags: C, python
Slug: properly-handling-the-keyboard-interrupt-exception-sigint-within-a-python-c-module

Recently I've done a lot of work requiring heavy computation on large datasets.
While python is not a great choice for speed, it can be extended by modules
written in C for those speed critical moments. For such moments I always try to
find solutions written as C modules. This approach works very well save for one
major caveat that seems to be common across many of the existing C modules.
This caveat has to do with the nonexistent handling of [SIGINT][], or the
KeyboardInterrupt exception, within the C module.

On linux, the SIGINT interrupt occurs when the user wishes to *cancel* a
command by pressing **ctrl+c**. Python properly receives this interrupt and
internally converts it to a [KeyboardInterrupt exception,][] thus in many cases
it's not necessary for the C module to handle SIGINT itself. However, in cases
where the C module function requires a significant amount of time, python will
not be able to handle the interrupt until the function call returns. Thus if
you are writing a C module with long running functions I suggest you implement
some sort of the following. One thing I want to mention: while this should
serve as a good example for those who want to write a python C module, please
do not think of this as a tutorial.

Let's start with a simple C program that computes the nth [Fibonacci][] number
using naïve recursion. This approach has an exponential running time and
therefore is perfect for demonstrating the want to end the process. You'll
notice in the code below that I have already added the SIGINT interrupt
handler. This handler normally would be redundant as C will terminate by
default when it receives SIGINT, however I added a simple print statement in
the interrupt handler to distinguish it from the default operation. I
acknowledge that it is a [bad practice][] to use printf in a signal handler,
however I am neglecting that concern for demonstration purposes.

    #include 
    #include 

    volatile sig_atomic_t kb_interrupt = 0;

    void kb_interrupt_handler(int sig) {
      printf("Received kb interrupt\n");
      kb_interrupt = 1;
    }

    int fibo(int n) {
      int a, b;
      if (kb_interrupt) return -1;
      else if (n < 2) return n;
      else if ((a = fibo(n - 1)) < 0) return -1;
      else if ((b = fibo(n - 2)) < 0) return -1;
      else return a + b;
    }

    int main() {
      int n;
      signal(SIGINT, kb_interrupt_handler);
      printf("Number: ");
      fflush(stdout);
      scanf("%d", &n);
      printf("Fibo(%d) = %d\n", n, fibo(n));
    }

Now let's convert this to something that python can use. In the code below,
you'll notice I eliminated the main function and the include statements as they
are no longer needed. All code that was added was needed to call the function
**fibo** from the python C module **bboe**.

    #include 

    volatile sig_atomic_t kb_interrupt = 0;

    void kb_interrupt_handler(int sig) {
      printf("Received kb interrupt\n");
      kb_interrupt = 1;
    }

    int fibo(int n) {
      int a, b;
      if (kb_interrupt) return -1;
      else if (n < 2) return n;
      else if ((a = fibo(n - 1)) < 0) return -1;
      else if ((b = fibo(n - 2)) < 0) return -1;
      else return a + b;
    }

    PyObject *bboe_fibo(PyObject *self, PyObject *args) {
      __sighandler_t prev;
      int n, result;
      if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
      prev = signal(SIGINT, kb_interrupt_handler);
      result = fibo(n);
      signal(SIGINT, prev);
      if (result < 0) {
        PyErr_SetObject(PyExc_KeyboardInterrupt, NULL);
        return NULL;
      }
      return Py_BuildValue("i", result);
    }

    PyMethodDef bboe_methods[] = {
      {"fibo", bboe_fibo, METH_VARARGS, "Compute the nth Fibonacci number."},
      {NULL, NULL, 0, NULL}
    };

    PyMODINIT_FUNC initbboe(void) {
      Py_InitModule("bboe", bboe_methods);
    }

The proper distutils setup.py script for this C module is shown below.

    from distutils.core import setup, Extension

    setup(name = 'BBoe',
          version = '1.0',
          ext_modules = [Extension('bboe', ['bboemodule.c'])])

Finally to reproduce the functionality of the C program I've written the
following. While you can copy and paste this code, you can also grab [this
tarball][] that contains all the code listed here, as well as a Makefile which
builds both the C and python parts. Simply run **make** followed by
**./fibo\_prog** for the C version, or **./fibo\_prog.py** for the python
version.

    #!/usr/bin/env python
    import bboe

    def main():
        try:
            n = int(raw_input('Number: '))
        except ValueError:
            n = 0
        try:
            res = bboe.fibo(n)
        except KeyboardInterrupt:
            res = -1
        print 'Fibo(%d) = %d' % (n, res)

    if __name__ == '__main__':
        main()

One last thing I want to mention is to ensure the signal handler is only
changed in your C module when required. In my first iteration of this code, I
had my call to **signal** in the **initbboe** method which had the negative
effect of using my **kb\_interrupt\_handler** whenever the **bboe** module was
loaded. The fix was to only have my signal handler in place whilst code from my
module was running. Lines 24 and 26 accomplish this properly.

Happy python C module coding!

<ins datetime="2010-09-15T22:13:25+00:00">
Edit 2010-09-15</ins>  
I wanted to test the speed between a pure C implementation, a python C module
implementation, and a pure python implementation. Thus I have updated [the
source tarball][this tarball] to include the following python file as well as a
script to generate the timing results which are also shown below.

    #!/usr/bin/env python

    def fibo(n):
        if n < 2: return n
        return fibo(n - 1) + fibo(n - 2)    

    def main():
        try:
            n = int(raw_input('Number: '))
        except ValueError:
            n = 0
        try:
            res = fibo(n)
        except KeyboardInterrupt:
            res = -1
        print 'Fibo(%d) = %d' % (n, res)

    if __name__ == '__main__':
        main()

`fibo(00) pure c: 0.002s c module: 0.016s pure python: 00.015s fibo(02) pure c: 0.002s c module: 0.014s pure python: 00.015s fibo(04) pure c: 0.002s c module: 0.014s pure python: 00.014s fibo(06) pure c: 0.002s c module: 0.015s pure python: 00.015s fibo(08) pure c: 0.002s c module: 0.015s pure python: 00.013s fibo(10) pure c: 0.002s c module: 0.017s pure python: 00.016s fibo(12) pure c: 0.002s c module: 0.013s pure python: 00.014s fibo(14) pure c: 0.002s c module: 0.015s pure python: 00.016s fibo(16) pure c: 0.002s c module: 0.014s pure python: 00.015s fibo(18) pure c: 0.002s c module: 0.014s pure python: 00.017s fibo(20) pure c: 0.002s c module: 0.014s pure python: 00.018s fibo(22) pure c: 0.002s c module: 0.012s pure python: 00.021s fibo(24) pure c: 0.003s c module: 0.013s pure python: 00.037s fibo(26) pure c: 0.004s c module: 0.017s pure python: 00.074s fibo(28) pure c: 0.008s c module: 0.020s pure python: 00.167s fibo(30) pure c: 0.018s c module: 0.027s pure python: 00.406s fibo(32) pure c: 0.034s c module: 0.040s pure python: 01.061s fibo(34) pure c: 0.067s c module: 0.080s pure python: 02.716s fibo(36) pure c: 0.167s c module: 0.183s pure python: 07.121s fibo(38) pure c: 0.425s c module: 0.450s pure python: 18.722s fibo(40) pure c: 1.099s c module: 1.153s pure python: 49.901s`

These results show first that there is much to be gained by writing a C module
for CPU intensive tasks, and second that a pure C implementation doesn't gain
you much in this particular case.

  [SIGINT]: http://en.wikipedia.org/wiki/SIGINT_(POSIX)
  [KeyboardInterrupt exception,]: http://docs.python.org/library/exceptions.html#exceptions.KeyboardInterrupt
  [Fibonacci]: http://en.wikipedia.org/wiki/Fibonacci_number
  [bad practice]: http://linux.die.net/man/2/signal
  [this tarball]: /images/2010/09/bboe_module.tgz
