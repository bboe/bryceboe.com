Title: New-buntu: Fesity Fawn
Date: 2007-04-22 14:52
Category: all
Slug: new-buntu-fesity-fawn

This last week was quite exciting mainly because [Ubuntu 7.04][] (Feisty Fawn)
was released. On the day it was released the Ubuntu repositories were a mess as
I'm sure everyone was downloading and updating so it at times was a painfully
slow process.

Once I finally had it downloaded I had [Adam][] burn me a CD of it as my burner
wasn't quite working, and then proceeded to install it. I was greatly hoping
for the most simplistic install possible, but alas I was wrong. Don't get me
wrong, for most Feisty will be painfully simple, however I run the x64 version
of Ubuntu and I have a Nvidia 8800 GTS which only has experimental linux
drivers (the same goes for Windows as well by the way).

As I wrote afterwards on Ubuntu Forums ([my post][]) I was successful in
installing via the standard x64 desktop cd and installing the beta drivers from
Nvidia. I hate to say it but it did take me awhile to figure out how to get it
working. I wont cover the details of getting it to work here, but simply
express my concern with User Friendly Linux and new hardware.

In my recent quest to get a patch into the Linux kernel I've discovered that
Linux distros (Ubuntu, Fedora, etc.) are behind the times as far as the kernel
is concerned. While this doesn't directly affect proprietary drivers (such as
Nvidia's video card drivers) as they aren't in the kernel, it does affect other
hardware developments, like how Ubuntu had terrible support for Wireless up
until now (I really hope it's fixed). The reason behind this is for stability
purposes distributions are a bit behind kernel development. My Ubuntu system is
currently running 2.6.20-15 which from the [debian change log][] this
corresponds to kernel version 2.6.20.3. [Kernel.org][] currently states the
latest vanilla (stable) kernel as 2.6.20.7. Though there is a very small
difference here Ubuntu Edgy's latest kernel version was 2.6.17.6. I may be
slightly wrong on the last digit however there has been significant changes
since 2.6.17.6 and 2.6.20.3 which corresponds to the need to release a new
Ubuntu version every 6 months.

But within it self this is a flaw, as people like myself who run hardware which
is new are forced to take extra steps to get it working properly. This is one
downside to the way linux works as even if Hardware developers started working
with the kernel developers changes wouldn't appear right away in a distribution
requiring people to compile their own kernels for new hardware.

Regardless the Ubuntu distribution has done excellent work in making Linux more
user friendly and I predict within five years Linux will be a major competitor
to Windows and Apple.

  [Ubuntu 7.04]: http://www.ubuntu.com
  [Adam]: http://www.adamdoupe.com
  [my post]: http://ubuntuforums.org/showpost.php?p=2495909&postcount=3
  [debian change log]: http://changelogs.ubuntu.com/changelogs/pool/main/l/linux-source-2.6.20/linux-source-2.6.20_2.6.20-15.27/changelog
  [Kernel.org]: http://kernel.org/
