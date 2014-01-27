Title: Time Zones in Python and Date/Time Representations
Date: 2012-11-05 01:57
Category: all
Tags: python, time zones
Slug: time-zones-in-python-and-datetime-representations

Early yesterday morning many people gained an extra hour by repeating the
second hour of the day. Those people in time zones that were previously on
[daylight saving time][] switched back to standard time and thus may have
observed their digital devices record the following sequence of times:

`2012-11-04 01:59:58 2012-11-04 01:59:59 2012-11-04 01:00:00 2012-11-04 01:00:01`

The written timestamps make it appear as if time went back one hour, when of
course time continued to proceed linearly. This perceived repetition of an hour
can be a problem for computer systems that output dates in localized formats.
For instance, python's logging package produces log entries using a
human-readable time. However, by [default][], these human readable times are in
localized formats. That means an event could be logged as happening before a
preceding event when the localized time zone experiences a change in daylight
saving time.

An obvious solution to this problem is to not take into consideration daylight
saving time when working with time. For people in the pacific time zone, that
could mean always using pacific standard time ([PST][]). Likewise for people in
the eastern time zone, they could always use eastern standard time ([EST][]).
Continuing with the log file example, this means all events in a log files will
appear linearly. The trade-off is anyone looking at log entries during daylight
saving time needs to keep in mind the one hour difference when determining how
long ago a logged event actually occurred.

A separate issue has to do with keeping track of dates and times between
machines in different time zones. For simplicity, we'll ignore the problem of
clock synchronization and assume all the machines have the correct time set.
The issue is that even when using standard times (non daylight saving times) on
respective machines, dates and times on different machines cannot be compared
in a human readable format without including time zone specific information.

Fortunately computers need not use a human readable format to store dates and
times. In fact, most computers already internally keep track of time using
[unix timestamps][] that store dates and times as the number of seconds since
an agreed upon date and time in coordinated universal time ([UTC][]). In spite
of this solution to synchronize dates and times from different time zones,
issues such as the logging problem still occur. In the remainder of this
article we will look at a few causes of those problems and how to solve them in
the context of python.

Within python there are two primary ways to store date and time information.
The first, is the unix timestamp, which was previously discussed. Although unix
timestamps are time zone agnostic, the major problem is that it is not simple
for a human to determine properties about a unix timestamp without first
converting to another format. For instance, what day of the month does the unix
timestamp `1325448000` represent? And, how many years does the previous unix
timestamp differ from `473414400`? To help answer such questions, programming
languages usually have a date and time representation that can be created from
unix timestamps. In python, this representation is accomplished through the
[datetime][] object:

`>>> from datetime import datetime >>> print(datetime.fromtimestamp(1325448000)) 2012-01-01 12:00:00 >>> print(datetime.fromtimestamp(473414400)) 1985-01-01 00:00:00`

Using the datetime representation you should be able to more easily answer the
previous questions. If you execute the above code, some of you might wonder why
`print(datetime.fromtimestamp(1325448000))` does not produce the same result on
your computer. The difference is due to the fact that datetime objects are
created in the context of the local time zone by default. On my system, the
local time zone is "America/Los\_Angeles", which corresponds to either PST or
PDT depending on the time of year. With that in mind let's look at instances of
datetime around the end of daylight savings time 2012.

`>>> a = datetime.fromtimestamp(1352019599) >>> b = datetime.fromtimestamp(1352019600) >>> print((b - a).total_seconds()) -3599.0`

Although the timestamp for *a* is one second less than the timestamp for *b*,
it appears as if *b* represents a time 3599 seconds (one second less than one
hour) prior to *a*. The reason is that, in addition to datetime objects using
the localized time zone by default, they do not maintain the time zone
information by default. Thus, naïve datetime objects, that is, those without
time zone information, are only compared by their values. Below are the values
for *a* and *b* from the previous example:

`>>> print(a) 2012-11-04 01:59:59 >>> print(b) 2012-11-04 01:00:00`

While these values are correct, we should also be able to compare them
correctly. Fortunately python's datetime objects allow us to also associate
time zone information. Unfortunately, the easiest way is through the
non-standard package [pytz][]. With pytz we can easily create time zone
specific datetime objects. Doing so will solve the comparison problem:

`>>> import pytz >>> a = datetime.fromtimestamp(1352019599, pytz.timezone('America/Los_Angeles')) >>> b = datetime.fromtimestamp(1352019600, pytz.timezone('America/Los_Angeles')) >>> print((b - a).total_seconds()) 1.0 >>> print(a) 2012-11-04 01:59:59-07:00 >>> print(b) 2012-11-04 01:00:00-08:00`

In the previous example we get a [tzinfo][] object by calling
`pytz.timezone('America/Los_Angeles')` and use that in creating the datetime
object. Note that the time zone selected only affects how the datetime object
is represented. Observe that the following two datetime objects are the same
despite their different representation:

`>>> a = datetime.fromtimestamp(1352019599, pytz.timezone('America/Los_Angeles')) >>> b = datetime.fromtimestamp(1352019599, pytz.timezone('America/New_York')) >>> a == b True >>> print(a) 2012-11-04 01:59:59-07:00 >>> print(b) 2012-11-04 03:59:59-05:00`

It should now be obvious that it is always a good idea to create datetime
objects with time zone information included. Two other common ways of creating
datetime objects with time zone information are
`datetime.now(pytz.timezone('America/Los_Angeles'))` to create a datetime
object of the current date and time and
`datetime(2012, 11, 4, 1, 0, tzinfo=pytz.timezone('America/Los_Angeles'))` to
create a datetime object for a specific date and time.

With time zone specific datetime objects, it's trivial to get a localized
representation for any time zone through the [astimezone][] function:

`>>> print(a) 2012-11-04 01:59:59-07:00 >>> print(a.astimezone(pytz.timezone('America/New_York'))) 2012-11-04 03:59:59-05:00 >>> print(a.astimezone(pytz.UTC)) 2012-11-04 08:59:59+00:00`

Thus far we've shown that using unix timestamps is great for date and time
consistency between machines at the cost of not being human readable. We then
gave a brief overview of datetime objects, including how to create them from
unix timestamps. Most importantly we showed that datetime objects are time zone
agnostic by default. We then showed how to include time zone information in
datetime objects and how to convert between various local datetime
representations. We will now show how to correctly convert from datetime
objects back to the correct unix timestamp.

In the python standard library there is nothing that directly converts from
datetime objects to unix timestamps. However, there are two functions,
[time.mktime][], and [calendar.timegm][] that will create timestamps from
[struct\_time][] objects. These functions, in combination with the datetime
[timetuple][] functions, allow for the conversion. The primary difference
between **time.mktime** and **calendar.timegm** is that **time.mktime** expects
the struct\_time object to store the date and time information in the system
localized time zone, whereas **calendar.timegm** expects the date and time
information to be stored in UTC.

Making no assumptions about the time zone the datetime object is currently
represented in, the following shows how to convert a datetime object to a unix
timestamp using **time.mktime**:

`>>> import time >>> import pytz.reference >>> a = datetime.fromtimestamp(1352019599, pytz.timezone('America/New_York')) >>> time.mktime(a.astimezone(pytz.reference.LocalTimezone()).timetuple()) 1352019599.0`

Notice that we must first convert the datetime object, *a*, into its identical
representation in our localized time zone before calling timetuple. The
`pytz.reference.LocalTimezone()` code prevents us from needing to hard-code our
localized time zone.

The second approach to convert from a datetime object to a unix timestamp is to
first convert to UTC and then use **calendar.timegm**:

`>>> import calendar >>> calendar.timegm(a.utctimetuple()) 1352019599`

When using **calendar.timegm** we can conveniently use the datetime
[utctimetuple][] function rather than using the astimezone function.

At this point you should have a decent grasp on converting between unix
timestamps and time zone sensitive datetime objects in the context of python
applications. If you are anything like me, you will now *always* create
datetime objects with time zone information and ponder why that is not the
python library default.

In a future blog post (if I ever get around to it) I will look at storing and
retrieving datetime objects in databases using sqlalchemy. A few questions I
have are:

-   When the python application and the database are in different time zones,
    how are the datetime objects represented?
-   What happens when either the database or the python application changes
    time zones?

That's all for now. Happy coding!

<ins datetime="2012-11-06T20:14:01+00:00">
Update</ins>: I just discovered that python 3.3 now has a `datetime.timestamp`
function which handles the conversion from datetime objects to unix timestamps
([source][]).

  [daylight saving time]: http://en.wikipedia.org/wiki/Daylight_saving_time
  [default]: http://docs.python.org/2/library/logging.html#logging.Formatter.formatTime
  [PST]: http://en.wikipedia.org/wiki/Pacific_Time_Zone
  [EST]: http://en.wikipedia.org/wiki/Eastern_Time_Zone
  [unix timestamps]: http://en.wikipedia.org/wiki/Unix_time
  [UTC]: http://en.wikipedia.org/wiki/Coordinated_Universal_Time
  [datetime]: http://docs.python.org/2/library/datetime.html#datetime-objects
  [pytz]: http://pytz.sourceforge.net/
  [tzinfo]: http://docs.python.org/2/library/datetime.html#datetime.tzinfo
  [astimezone]: http://docs.python.org/2/library/datetime.html#datetime.datetime.astimezone
  [time.mktime]: http://docs.python.org/2/library/time.html#time.mktime
  [calendar.timegm]: http://docs.python.org/2/library/calendar.html#calendar.timegm
  [struct\_time]: http://docs.python.org/2/library/time.html#time.struct_time
  [timetuple]: http://docs.python.org/2/library/datetime.html#datetime.date.timetuple
  [utctimetuple]: http://docs.python.org/2/library/datetime.html#datetime.datetime.utctimetuple
  [source]: http://docs.python.org/dev/library/datetime.html#datetime.datetime.timestamp
