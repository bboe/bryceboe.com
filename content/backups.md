Title: Backups
Date: 2009-04-06 17:53
Category: all
Tags: s3, unix commands
Slug: backups

I turned my computer on this morning and to my dismay my 9 month old 1TB
harddrive could no longer be detected. It is still under warranty so
it's no big deal about the hardware going bad, however it is a big deal
that I didn't have a backup of anything on the drive. Fortunately it
only consisted of replaceable content, however it will take quite some
time and bandwidth to regain that content.

This drive failure emphasizes the importance of backing up my
unrecoverable data, and I'm curious as to what methods other people use
for backup. A few months ago I backed up a good amount of information to
Amazon S3, however doing that on a regular basis is not the simplest
task, and probably isn't the best place to store sensitive information
unless it's encrypted. The other thing that's important to me is
synchronization between my desktop and laptop, of which the challenge is
my laptop runs OS X and my desktop runs Ubuntu Linux. I currently use
rsync to move files back and forth, however it's not a good solution
when I wish to delete or rename files. I also am considering using GIT
to store version information which so long as only 1 is considered the
master there should be no issues.

Also on a semi-related note, if you want to run **make clean** on any
folder under your current one which contains a makefile for archiving
purposes try the following command:  

`find . -iname Makefile -exec dirname {} \; | while read i; do make clean -C $i; done`
