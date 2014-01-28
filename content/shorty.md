Title: Shorty
Date: 2007-03-22 02:31
Category: all
Slug: shorty

This is a quick post as I feel a need to brag a bit about my recent
accomplishment, but first a short list of what's been going on.

-   Midterms
-   Papers
-   Programming Assignments (I wrote a compiler)
-   GRE Test
-   Apply to UCSB's Computer Science 5th year Master Program
-   And now finals

Yes it's finals week and tomorrow I have two and thus I should be studying, but
anyone that's read these blog entries may notice that I usually write around
times when I *should* be doing something else.

Anyways in addition to what was listed I began testing various python windowing
toolkits and I expect to write a lengthy comparison of the following:

-   pyGTK
-   pyQT
-   tkinter
-   wxpython

My comparison will include information on development of each of these in
windows and in linux, and how the end result appears on both. It should be
fairly decent and hopefully will attract some more random googlers to my site.

And now the big news, or at least what I feel is big. I am running on my own
compiled linux vanilla kernel version 2.6.20.3 to be exact. This was yet
another project to distract me from studying for finals, however I think this
one may pay off. I made it my goal to get a patch into the linux kernel by the
end of this year. Though from what I'm reading this sounds to be somewhat
difficult given many good patches are rejected, I'm confident I'll find
something to do that will get in there.

Now this may be a premature assumption however I feel that contributing to the
linux kernel is a great way to boost a resume, and especially a great way to
learn the inter workings of linux.

On a side note I want to post a few things about my build process. Since I use
Ubuntu as my main distro I decided to use the make-kpkg command rather than
make for the builds. The benefits of this are package management and automatic
installation, thus allowing me to easily undo an install. The main tip I picked
up which most people appear to have wrong is the following:

Don't use the /usr/src directory for your sources. The directory is owned by
root and the kernel should not be made with root privileges, thus using
/usr/src is not recommended. Create a ~/src directory and work from there.

Also in order to make use of a multi core processor in make-kpkg one must run
the following command:

`export CONCURRENCY_LEVEL=4`

This calls make using the -j command (number of jobs) which cannot be passed to
make-kpkg. Since I have a dual core computer 4 is a good number of jobs as it
allows each core to process two jobs. I can't really say if 4 is a better
option than two but it certainly is faster than 1 which is the default.

Anyways I guess that's it. I'll try to get that python windowing toolkit
comparison up soon.
