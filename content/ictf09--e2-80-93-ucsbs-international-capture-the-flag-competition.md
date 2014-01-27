Title: iCTF09: UCSB's International Capture the Flag Competition
Date: 2009-12-06 00:45
Category: all
Tags: hacking, python
Slug: ictf09-%e2%80%93-ucsbs-international-capture-the-flag-competition

As a member of the Security Lab at UCSB I had the privilege to help create and
run this year's [iCTF][] Hacking Competition. The six-year-old competition was
very unique this year. Unlike CTFs seen before in which teams try to protect
their services whilst attacking other teams' services, our competition had
teams deliver [drive-by downloads][] to users for the purpose of stealing money
from the users' bank accounts.

In order to deliver drive-by downloads, the teams had to bring users to their
webpage by boosting their search result on the search server for desired search
terms. The users' browsing pattern was they would search for a random word from
a news site and then visit one of the resulting pages chosen according a
[Pareto distribution][], meaning the top search result would have the highest
probability of being picked with the last result the lowest.

The challenge there was to figure out how to boost the search results for
particular keywords, unfortunately most of the teams simply duplicated the news
site; this definitely was the safest strategy though slightly disappointing to
me as I wrote the search engine code. I can claim that neither the search
engine, nor the index server broke during the competition. The crawler had a
few issues with some team's pages, which I quickly fixed. I have made the
[search engine code][] available that was used in iCTF09.

In addition to writing the search engine, I wrote three challenges for the
competition. The first challenge I wrote was called "The Difference", or
Forensics 4. The only information people were given was the title and the
following image. The first step to solve this challenge is recognizing the
image is the [xkcd][] comic "[The Difference][]".

[![The Difference][1]][]After downloading the original image one should notice
the two files are different sizes with the original being 32KB and my image
46K. At this point a pixel-by-pixel comparison is required which reveals that
60 of the pixels differ and the values of the differing pixels are always
larger in my image. This is where "The Difference" first comes into play by
subtracting the value in my image from that of the original.

Doing so produces the results shown in [the\_difference\_values.txt][]. Each
line contains the difference value and the index of the pixel. The values in
this list range from 33 to 41 with exceptions 10, 12 and 15. Additionally the
numbers appear in groups of three where last number in the group is sometimes
larger. After a bit of pondering the realization sets in that [ASCII][]
lowercase values range from 97 to 122 with space being 32 and hyphen 45. It
should hit you like a ton of bricks that you need to sum the groups of three
together and then convert the number to its ASCII value.

The string "sixty-four seventeen" now appears and you think you've solved the
challenge, but no, it's not quite done. This is where "The Difference" comes
back into play in that you have to subtract these two numbers to get
forty-seven. There were 596 submissions for this challenge of which 2 were
correct. I've made the source to both [generate][] and [verify][] this
challenge available.

The second challenge I wrote had 75 submissions and 0 correct solutions. This
challenge was one of the Trivia 3 problems that had a [text file][] and the
following blurb associated with it:

> Rummaging through the attic one afternoon Sally found a notebook which on the
> cover read 'What happened in 95?'. On one of the pages she found the
> following two paragraphs of text which appeared as gibberish to her. She
> copied the two paragraphs down as best she could, however there were
> forty-five characters which she couldn't make out from the first paragraph,
> which she simply neglected. What are those 45 characters?

The concept behind this problem is a [one-time pad][], where a completely
random sequence of characters the same length as the original text is generated
and then [XOR][]ed with the original text to create the cipher text. At this
point the original text can be discarded and recovered by XORing the cipher
text with the one-time pad.

The challenge to this problem is finding where the 45 missing characters go,
and what they are. One additional difficulty is figuring out that the ASCII
values need to be subtracted by 95 prior to XORing so the numbers being XORed
fit within 32 bits. This can be discovered by taking the min value that appears
in the paragraphs which is 95 corresponding to '\_' and additionally the max
value that appears which is 126 corresponding to '\~'. The '95' that appears in
the blurb was to hint at this.

Finding the places where the characters should go requires XORing the current
one-time pad with the cipher text. Plain text English with no punctuation or
spaces will result at the beginning of the output until nonsense text is
output. This is the point in which a character needs to be added to the
one-time pad. This process needs to be repeated for all 45 characters.

At this point, XORing the one-time pad character with the desired character
will result in the missing character. The solution is the concatenation of all
the missing characters. This is "sdnalsilennahcehtdnuoradnuofebnacsehcnarbidun"
which is "nudibranchescanbefoundaroundthechannelislands" reversed.

I've made the [code to generate][] this challenge available. You'll notice it
loops until the one-time pad contains the characters of the solution. The
[original text][] is a passage from [Joyce's][] [Dubliners][] that contains the
oldest reference I know of to the phrase, "[how goes it][]". I did not write a
solution for this problem.

The third and final problem I wrote was called 0xDEAFBABE or Trivia 2. A
[binary file][] (renamed to include .mid to resolve content type issues) was
provided which the program file correctly informs that it is a midi audio file.
By playing the file one hears about one note a second. Many teams tried to
figure out what the notes were as they would be on a musical scale, such as c
sharp or b flat, however that was a bit over thinking it. The solution was
simply to print the ASCII character that corresponds to each [midi note
number][]. These numbers range from 0 to 127, thus they're perfect for text.
The solution to this was "does this not sound super cool?" There were 207
submissions of which 21 were correct. I have made my source to [generate][2]
and [verify][3] this challenge available.

If you competed in the iCTF and attempted or completed any of these challenges
let me know what you thought and how long you spent on them. I recall someone
in the chat yesterday saying they were losing their sanity trying to solve "The
Difference"; that gave me a good laugh :)

  [iCTF]: http://ictf.cs.ucsb.edu/
  [drive-by downloads]: http://en.wikipedia.org/wiki/Drive-by_download
  [Pareto distribution]: http://en.wikipedia.org/wiki/Pareto_distribution
  [search engine code]: http://cs.ucsb.edu/~bboe/public/ictf09/search_engine.tar.gz
  [xkcd]: http://xkcd.com/
  [The Difference]: http://xkcd.com/242/
  [1]: /images/2009/12/the_difference-159x300.png "The Difference"
  [![The Difference][1]]: /images/2009/12/the_difference.png
  [the\_difference\_values.txt]: http://cs.ucsb.edu/~bboe/public/ictf09/the_difference_values.txt
  [ASCII]: http://en.wikipedia.org/wiki/ASCII
  [generate]: http://cs.ucsb.edu/~bboe/public/ictf09/the_difference_maker.py
  [verify]: http://cs.ucsb.edu/~bboe/public/ictf09/the_difference_checker.py
  [text file]: http://cs.ucsb.edu/~bboe/public/ictf09/theparagraphs.txt
  [one-time pad]: http://en.wikipedia.org/wiki/One-time_pad
  [XOR]: http://en.wikipedia.org/wiki/Exclusive_or
  [code to generate]: http://cs.ucsb.edu/~bboe/public/ictf09/otp_creator.py
  [original text]: http://cs.ucsb.edu/~bboe/public/ictf09/otp_text.txt
  [Joyce's]: http://en.wikipedia.org/wiki/James_Joyce
  [Dubliners]: http://en.wikipedia.org/wiki/Dubliners
  [how goes it]: http://www.urbandictionary.com/define.php?term=how+goes+it
  [binary file]: http://cs.ucsb.edu/~bboe/public/ictf09/0xDEAFBABE.mid
  [midi note number]: http://www.midi.org/techspecs/midimessages.php
  [2]: http://cs.ucsb.edu/~bboe/public/ictf09/midi_generation.py
  [3]: http://cs.ucsb.edu/~bboe/public/ictf09/midi_checker.py
