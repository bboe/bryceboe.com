Title: Random Lines from a File
Date: 2009-03-23 01:36
Category: all
Tags: google, interview question, python
Slug: random-lines-from-a-file

<ins datetime="2011-07-19T04:55:09+00:00">
**Update 2011-07-18**: As Ernesto correctly points out in the comments, this
algorithm selects N *independent* random lines from a file.</ins>

The following is my python implementation of choosing N random lines with equal
probability from a file. This implementation is both memory and time efficient
unlike other solutions. This problem was originally brought to my attention
after a friend was asked a similar problem at a Google interview. Additionally
a few weeks ago I was catching up on [Jonathan's blog][] and came across his
[March 2008 post][] about this problem. I submitted a similar solution to the
one below in his comments.

Anyway, a naïve solution to this problem involves calculating a random position
in the file, with the file size being the max. However this solution does not
give equal probability to each line as longer lines will more likely be
selected.

The simple solution involves counting the number of lines in the file and then
choosing N random lines. However this requires a scan over the entire file to
count the number of lines, and then in the worst case an entire scan over the
file to print each random line. This is time inefficient if the file is massive
in size.

One optimization is to store the seek position of all the line indexes in
memory, thus avoiding the scanning to print out each random line. However this
requires storing a number for all the lines in the file, which is memory
inefficient if the file has a ton of lines.

By choosing whether to keep or replace the selected lines at each step in a
single scan, one simply needs to store N positions into the file thus being
both time and memory efficient. I'll leave the exercise of proving that each
line is selected with equal probability up to you.

<ins datetime="2009-03-23T16:19:43+00:00">
Edited: Added prev so that the first line would be included, and replaced
file.readline()[:-1] with file.readline().strip() to remove trailing whitespace
properly.</ins>

    :::python
    #!/usr/bin/env python
    import os, random, sys

    if __name__ == '__main__':
        def error_exit(msg):
            sys.stderr.write(msg)
            sys.exit(1)

        # Verify arguments
        if len(sys.argv) != 3: error_exit('Usage: %s FILE NUM_LINES\n' %
                                          os.path.basename(sys.argv[0]))
        text_file = sys.argv[1]
        if not os.path.isfile(text_file):
            error_exit('%s does not exist, or is not a file\n' % text_file)
        try:
            num_lines = int(sys.argv[2])
        except ValueError:
            error_exit('%s is not a number\n' % sys.argv[2])

        seeks = [0 for x in range(num_lines)]
        file = open(text_file)
        count = 0
        prev = 0

        # Calculate Random Lines
        while file.readline():
            for i in range(num_lines):
                if random.randint(0, count) == 0:
                    seeks[i] = prev
            prev = file.tell()
            count += 1

        # Print Random Lines
        for i, pos in enumerate(seeks):
            file.seek(pos)
            print '%d: %s' % (i, file.readline().strip())

        file.close()

  [Jonathan's blog]: http://jmkupferman.blogspot.com/
  [March 2008 post]: http://jmkupferman.blogspot.com/2008/11/read-random-line-in-large-file-in.html
