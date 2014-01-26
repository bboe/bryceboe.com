Title: Line Segment Intersection Algorithm
Date: 2006-10-23 19:59
Category: all
Tags: python
Slug: line-segment-intersection-algorithm

November 11th I'll be participating in the [Southern California
Regional][] [ACM][] [programing competition][]. This is my second time
competing as well as [Adam's][]. One of our [practice problems][]
involved finding if a wall blocks the path between two points. At the
time the only way I could think of doing this involved solving for the
intersection, and then checking to make sure the intersection point is
contained within the domain and range of both segments.

Upon looking at the [solution][] I noticed whoever wrote it had a method
called signedarea which I was determined to figure out as the solution
was much more elegant than mine. After searching this morning I came
across a [simpler way][] (and [this][]) to determine if two line
segments intersect.

The solution involves determining if three points are listed in a
counterclockwise order. So say you have three points A, B and C. If the
slope of the line AB is less than the slope of the line AC then the
three points are listed in a counterclockwise order.

This is equivalent to:

~~~~ {lang="python"}
def ccw(A,B,C):
    return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)
~~~~

You might be wondering how does this help? Think of two line segments
AB, and CD. These intersect if and only if points A and B are separated
by segment CD and points C and D are separated by segment AB. If points
A and B are separated by segment CD then ACD and BCD should have
opposite orientation meaning either ACD or BCD is counterclockwise but
not both. Therefore calculating if two line segments AB and CD intersect
is as follows:

~~~~ {lang="python"}
def intersect(A,B,C,D):
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
~~~~

I've created a [python script][] which demonstrates this algorithm.

  [Southern California Regional]: http://www.socalcontest.org/
  [ACM]: http://www.acm.org/
  [programing competition]: http://icpc.baylor.edu/icpc/
  [Adam's]: http://www.adamdoupe.com
  [practice problems]: http://www-rcf.usc.edu/~dkempe/contest/fall06/fall06.pdf
  [solution]: http://www-rcf.usc.edu/~dkempe/contest/fall06/ee.c.txt
  [simpler way]: http://compgeom.cs.uiuc.edu/~jeffe/teaching/373/notes/x06-sweepline.pdf
  [this]: http://compgeom.cs.uiuc.edu/~jeffe/teaching/373/notes/x05-convexhull.pdf
  [python script]: /wordpress/wp-content/uploads/2006/10/intersect.py
