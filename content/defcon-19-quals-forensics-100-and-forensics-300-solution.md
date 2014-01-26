Title: Defcon 19 Quals Forensics 100 and Forensics 300 Solution
Date: 2011-06-05 19:18
Category: all
Tags: hacking, python
Slug: defcon-19-quals-forensics-100-and-forensics-300-solution

For the third year, I competed with team Shellphish in the Defcon quals.
We pulled through with some amazing points at the end to finish in [8th
place][]. My successful contributions, however, were really only with
respect to Forensics 100 and 300. My write up for the following are
below:

**Forensics 100**  
The forensics 100 challenge indicated to find the key, and [provided a
png file][] that was 19025x1 in resolution. Immediately our team thought
we could simply change the resolution to [25x761][] and would be on to
something. After working with the resulting image for sometime I finally
thought about converting it to [761x25][]. That was our first break
through when we read some text along the lines of
"ILoveMeSomesheepysheepies" followed by binary that includes capital
'O's in place of some of the '0's. After no success with different
permutations of that message we incorporated an idea the other team
members had about the blue offset pixels that occur at regular
intervals. Our first attempt at wrapping the image at the blue pixel
boundaries (every 450 pixels) [resulted in success][]! The key
"thankYouSirPleasemayIhaveAnother" appeared and worked. The following is
my simple python solution for Forensics 100:

~~~~ {lang="python" line="1"}
#!/usr/bin/env python
import sys, Image

def main():
    orig = Image.open('f100.png')
    img = Image.new('RGBA', (450, 43))
    img.putdata(orig.getdata())
    img.show()

if __name__ == '__main__':
    sys.exit(main())
~~~~

**Forensics 300**  
Forensics 300 was quite an interesting challenge. I don't have the
original file, nevertheless, one had to extract the initial file with a
password to get a dmg containing a dump from an iphone. I came into the
challenge a little late, after one of my teammates had gone through all
the images, videos, and audio files looking for Waldo and 'grep'ing for
various relevant keywords. Further more, my teammates had previously
used the [iPhoneTracker][] on the consolidated.db file to see where the
phone had been, however San Antonio didn't prove to be very useful.

While the iPhoneTracker app seemed pretty cool, I wanted to
programmatically see where the phone had been the most. Thus, after
figuring out what was what with respect to the consolidated.db file I
wrote a little python script to find the most visited places rounded to
less precision to account for some variance. The top three results were
the following where the first number represents the number of
occurrences in that location, and the two numbers between the
parenthesis represent the latitude and longitude respectfully.

-   30 ('-77.846', '166.677')
-   18 ('0.000', '0.000')
-   10 ('36.106', '-115.173')

When I did a [google search for the coordinates -77.846 166.667][] I
knew immediately that it was no coincidence that I was centered in a
small town in Antarctica. Unfortunately, Google maps doesn't have a name
for this location so I had to [revert to Bing][] (for the first time
ever) to figure out that this location is called Ross Island. From that
point we simply attempted different "places" listed [Ross Island's
wikpiedia page][] until "McMurdo Station" submitted successfully. Below
is the script I used to find the coordinates from the [consolodated.db
input file][]:

~~~~ {lang="python" line="1"}
#!/usr/bin/env python
import os, sys

def main():
    os.system('sqlite3 consolidated.db "select Latitude, Longitude '
              'from CellLocation;" > tmp')
    
    uniq = {}
    for line in open('tmp'):
        pos = tuple('%.3f' % float(x) for x in line.split('|')[:2])
        if pos in uniq:
            uniq[pos] += 1
        else:
            uniq[pos] = 1

    for pos, count in sorted(uniq.items(), key=lambda x:x[1]):
        print count, pos

if __name__ == '__main__':
    sys.exit(main())
~~~~

You can find links to solutions to other Defcon 19 Quals challenges at
the following locations: [Rogunix][], [negative foo][], [VNSecurity
site][].

  [8th place]: http://stalkr.net/defcon/graph.htm
  [provided a png file]: http://www.bryceboe.com/wordpress/wp-content/uploads/2011/06/f100.png
  [25x761]: http://www.bryceboe.com/wordpress/wp-content/uploads/2011/06/f100_25_761.png
  [761x25]: http://www.bryceboe.com/wordpress/wp-content/uploads/2011/06/f100_761_25.png
  [resulted in success]: http://www.bryceboe.com/wordpress/wp-content/uploads/2011/06/f100_solution.png
  [iPhoneTracker]: http://petewarden.github.com/iPhoneTracker/
  [google search for the coordinates -77.846 166.667]: http://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=-77.846+166.677&sll=-77.578778,167.409668&sspn=1.030596,5.218506&ie=UTF8&t=h&z=15
  [revert to Bing]: http://www.bing.com/maps/?v=2&where1=-77.846%20166.677
  [Ross Island's wikpiedia page]: http://en.wikipedia.org/wiki/Ross_Island
  [consolodated.db input file]: http://www.bryceboe.com/wordpress/wp-content/uploads/2011/06/consolidated.db
  [Rogunix]: http://rogunix.com/defconquals19.html
  [negative foo]: http://t.negativefoo.org/post/6235620215/dc19-ctf-quals-writeups
  [VNSecurity site]: http://www.vnsecurity.net/2011/05/defcon-19-ctf-quals-writeups-collection/
