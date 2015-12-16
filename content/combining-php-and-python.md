Title: Combining PHP and Python
Date: 2006-11-07 13:32
Category: all
Tags: priceTrackr, python
Slug: combining-php-and-python

I've been writing code in [php][] for three years now, and within the last year
discovered the [python][] language. Without going into much detail I find
myself utilizing python more so than php. I do have things I dislike about
python (mainly its [documentation][] as compared to [php's][]) but for the most
part it appears superior to php for command line scripting. I guess there
weren't any doubts about that since php is used mostly as an apache module.

Making priceTrackr's update scripts run faster has presented me with a problem.
My update scripts were originally written in php as my web host will not
install the [mysql-python][] module. Not easily being able to connect to my
database made python useless for this purpose and thus I used php. Now that my
update process is taking over an hour to complete it has come time to optimize
the code. The solution is threading.

Threading allows me to open multiple web connections at once to speed up the
processing time. The problem here is that php does not have threading support;
this is where python comes back into the picture. Python has decent thread
support; I say decent because it could be much better (doesn't make use of
multiple processors). Threading in python is handy when waiting on input such
as that from a URL request, and is not useful for CPU intensive calculations
because it does not span threads over multiple processors.

Since I need php to interface with mysql and python for its threading support I
came up with the following solution:

1.  Use php to get the information needed from the database.
2.  Pass that information to python to be processed in a threaded manor.
3.  Return processed information to php to be stored in the database.

I accomplished this with a primary shell script, two php scripts, and a python
script. In addition to my priceTrackr update scripts I've created an example
set which follows the same behavior to be used as a tutorial for python
threading as well as combining python and php.

The example behaves as follows:

**main.sh**

This file calls each of the following files by piping the output of each to the
next. The file also displays the total running time in seconds when completed.

view [main.sh][]

**phpPart1.php**

This file represents getting needed data from the database. The file itself
creates md5hashes for the strings representing numbers 1-3000. Each hash is
printed out on its own line.

view [phpPart1.php][]

**python.py**

This file is where all the magic happens. In my update scripts this file would
make a URL connection and then process the page. In this example the script
brute forces each hash to get the original number. The final output is each
hash followed by a tab followed by the number the hash represents.

This file makes use of python's [Queue][] class for blocking purposes. I
commented the code so it should be fairly easy to understand and simple enough
to modify for your python threading needs.

view [python.py][]

Note: Since this is a process intensive script multi threading doesn't decrease
runtime. This is just used for a simple example of python threading.

**phpPart1.php**

This file verifies that the returned data is valid. If at any point something
is invalid the script exits. If all data is valid it prints 'Completed!'.

view [phpPart2.php][]

The whole package with proper extensions can be downloaded:

[phpPython][]

  [php]: http://php.net
  [python]: http://python.org
  [documentation]: https://docs.python.org/2/library/
  [php's]: http://www.php.net/manual/en/
  [mysql-python]: http://sourceforge.net/project/showfiles.php?group_id=22307
  [main.sh]: /images/2006/11/main.txt
  [phpPart1.php]: /images/2006/11/phppart1.txt
  [Queue]: https://docs.python.org/2/library/queue.html
  [python.py]: /images/2006/11/python.py
  [phpPart2.php]: /images/2006/11/phppart2.txt
  [phpPython]: /images/2006/11/phppython.tgz
