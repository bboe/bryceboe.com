Title: Dynamic Programming - Coin Change Problem in Python
Date: 2009-11-04 22:35
Category: all
Tags: python
Slug: dynamic-programming-%e2%80%93-coin-change-problem-in-python

<ins datetime="2011-02-25T20:06:41+00:00">**Update 2011/02/25 12:07**  
Updated the code such that it doesn't rely on a coin of denomination
one.</ins>

I assisted in hosting the UCSB Programming Competition again this year.
Doing so rekindled my love for dynamic programming algorithms, thus why
I prepared an example similar to this one for my class and why I wrote
this post.

In my own words, dynamic programming is a technique to solve a problem
in which previous solutions are used in the computation of later
solutions. The generic coin change problem is, given coins of a
specified denomination and a number N what are minimum number of coins
needed to make change for N? If you don't like my definitions see
wikipedia for [dynamic programming][] and [coin problem][].

You might be asking yourself, why is this even difficult; don't I always
just take the largest coin possible, as is done when making change with
US coins? You're right, that approach works with US coins and this
approach is called a greedy approach. However, if the coins are of value
*1*, *3*, and *4* then the greedy approach would say the best way to
make change of *6* is with three coins: *4*, *1* and *1*. As you've
probably figured out the correct, or optimal solution is with two coins:
*3* and *3*.

As I'm very fond of python I coded up a solution which should work in
any circumstance so long as *1* is one of the coin denominations. The
solution works as follows: Calculate the minimum number of coins to make
*1*, *2*, *3*, â€¦, all the way up to the number we want to make change
for. At any given point, *i*, the minimum number of coins to make *i* is
dependent upon previous solutions.

I'm going to be kind of lazy and not actually explain the process as the
code is pretty self explanatory, with one addition: The code doesn't
just calculate the minimum number of coins, but rather calculates what
coins were used to make the minimum at each point. See the code below.

~~~~ {lang="python" line="1"}
#!/usr/bin/env python
import os, sys

def solve_coin_change(coins, value):
    """A dynamic solution to the coin change problem"""

    table = [None for x in range(value + 1)]
    table[0] = []
    for i in range(1, value + 1):
        for coin in coins:
            if coin > i: continue
            elif not table[i] or len(table[i - coin]) + 1 < len(table[i]):
                if table[i - coin] != None:
                    table[i] = table[i - coin][:]
                    table[i].append(coin)

    if table[-1] != None:
        print '%d coins: %s' % (len(table[-1]), table[-1])
    else:
        print 'No solution possible'


if __name__ == '__main__':
    def usage():
        sys.stderr.write('Usage: %s value\n' % os.path.basename(sys.argv[0]))
        sys.exit(1)

    # Modify this to alter the denominations of coins
    coins = [1, 3, 4]

    if len(sys.argv) != 2:
        usage()
    try:
        value = int(sys.argv[1])
    except ValueError:
        usage()
    solve_coin_change(coins, value)
~~~~

  [dynamic programming]: http://en.wikipedia.org/wiki/Dynamic_programming
  [coin problem]: http://en.wikipedia.org/wiki/Coin_problem
