Title: A Day With Digg: priceTrackr was Dugg
Date: 2006-09-07 10:46
Category: all
Tags: priceTrackr
Slug: a-day-with-digg-pricetrackr-was-dugg

Yesterday was quite an exciting day as [priceTrackr][] made its presence
known with the help of my favorite news site [Digg][]. Excitement,
anger, and frustration carried me through the day. The following is a
reenactment of the events leading to, and of yesterday.

**9/5/2006 - 10:25AM**

I suggested to Adam that I should self promote priceTrackr on Digg,
which he initially spoke against it because it would be more reputable
from someone else. I agreed, however I was only hoping to attract a few
users from Digg, so I decided to go forward with it. Since I was only
expecting 10-20 diggs on this I figured it would be best to digg to my
blog entry allowing for someone in the future to digg priceTrackr
directly. In the long run this was a good and bad move on my part,
however I'll explain this later.

**9/5/2006 @ 10:48AM**

I submitted my [Official priceTrackr Launch][] article to Digg, which
Adam then quickly posted a direct link in the comments, and, of course,
dugg it. [Here's the Digg article][].

**9/5/2006 @ 10:56AM**

priceTrackr had already received 6 diggs, and Adam said, "I hope your
WordPress doesn't crap out." I though that it'd suck to be a victim of
[the Digg Effect][]" so I downloaded the [wp-cache plugin][] and tested
it's functionality. I had to fix one line in the code to get it to
display the page if there was no cached version. In addition Adam
pointed me to the [Digg This plugin][], which I figured would be cool to
have on the site.

**9/5/2006 @ The remainder of the day**

priceTrackr had shot up to about 12 diggs rather quickly, but then
settled down so I was only expecting few more however I was resilient to
let the article just sit there. I made an effort to make a semi-meaning
full comment every few hours so that the article would reappear in the
[Digg Spy][].

**9/6/2006 @ About 9:30AM**

Adam and I had went to the office for our day job and we were casually
checking the progress and noticed the article had about 30 diggs. About
this time I received a ton of emails from my update script indicating it
couldn't connect to [www.newegg.com][]. Turns out Newegg's www prefix
didn't work but [newegg.com][] had worked just fine, so I fixed my
problem.

**9/6/2006 @ Approximately 10AM**

Still checking the status Adam and I noticed there was about 40 diggs
and a user [herrshuster][] made the comment, "Lt's gt this on th front
page, diggrs!" I was still skeptical about making it to the front page
as nearly a day had passed, nonetheless my excitement level had gone way
up, and my day job work for that day pretty much stopped.

**9/6/2006 @ About 10:30AM (The Big Bang)**

I was constantly checking the most popular page of upcoming tech
articles and upon refresh my article had disappeared from the top of the
list. My excitement peaked, I yelled something similar to  
[the Dean Scream][], and immediately went to check on the comments.

**9/6/2006 @ 10:35AM**

Though I was filled with excitement I soon realized that my host
probably can't handle the large influx of people on priceTrackr, as I
had not enabled any sort of caching. I sent an email to my host
requesting they do all that is possible to keep my server running.

**9/6/2006 @ 10:36AM**

The Digg Effect was in full effect as my host as disabled my account. I
immediately called their technical service to resolve this,
unfortunately paying $6/month doesn't give you much flexibility in what
can be done. They said they'd turn it back on, however they'd have to
chmod my priceTrackr folder until the traffic subsided. I asked them to
put up a message stating the site was down and politely hung up the
phone despite my terrible frustration at the time.

At this point I wasn't sure what to do as I didn't want to spend
$99/month on a dedicated host when I wouldn't need it within a week, but
I wanted to get my site back up as soon as possible. Adam suggested
using the company's dedicated host temporarily, and that is what I did.

Comments on my blog started coming in stating my site was down; like I
didn't know. My personal favorite was from ted who wrote, "[your site is
down, probably will never visit again. nice knowing you][]."

**9/6/2006 @ 11AM**

I changed my DNS servers to point to the updated DNS, and made the
necessary changes on the host to allow my site to be reached. I then
moved the files and the database over, and finally waited for people's
DNS to update.

**9/6/2006 @ 1:19PM**

I [posted][] in my comments that priceTrackr was back up, however I
forgot to mention that it only applied for people who's DNS had received
the update.

**9/6/2006 @ The rest of the day**

The diggs kept going up and people visited both this site was well as
priceTrackr. Of course some people weren't able to get to priceTrackr
well into the evening, but there wasn't much I could do about that.
After all the excitement a delayed hangover set in, so no day job work
was accomplished.

Later that night I implemented [pear's Cache\_Lite][] (I am a proud
supporter of the pear packages), which to my surprise was amazingly
simple and greatly decreased the server load, as well as the page
loading time.

**Results of being dugg**

I mentioned before digging to my blog was both good and bad, and here is
why: Digging to my blog was beneficial because this site was down for
approximately 10 minutes where priceTrackr was down at least two hours
or more depending on the user's DNS. The negative side of this was I
received about two times as many visitors to my blog than I did to
priceTrackr. I know this has to do with priceTrackr being unreachable,
but nonetheless those people did not get to see priceTrackr.

Traffic graph of bryceboe.com  
![Bryce Boe Traffic Graph][]

Traffic graph of priceTrackr.com  
![priceTrackr Traffic Graph][]

As you can see priceTrackr had two spikes which definitely hurt the
amount of traffic that visited the site. For those of you that are
wondering I made about $20 from [Google Adsense][] yesterday which isn't
too shabby. If I can consistently pull in at least $5 a day I will
upgrade to a dedicated host.

Finally I just want to thank everyone who dugg priceTrackr despite the
self promotion. I hope priceTrackr will be useful and there is anything
that you would like to see please send me an email or make a comment.
You may check on the status of priceTrackr at the [priceTrackr project
page][]. Thanks again.

  [priceTrackr]: http://www.pricetrackr.com
  [Digg]: http://www.digg.com
  [Official priceTrackr Launch]: /2006/08/27/official-pricetrackr-launch/
  [Here's the Digg article]: http://www.digg.com/tech_deals/Newegg_priceTrackr
  [the Digg Effect]: http://en.wikipedia.org/wiki/Slashdot_effect
  [wp-cache plugin]: http://mnm.uib.es/gallir/wp-cache-2/
  [Digg This plugin]: http://www.aviransplace.com/index.php/digg-this-wordpress-plugin/
  [Digg Spy]: http://www.digg.com/spy
  [www.newegg.com]: http://www.newegg.com
  [newegg.com]: http://newegg.com
  [herrshuster]: http://www.digg.com/users/herrshuster
  [the Dean Scream]: http://en.wikipedia.org/wiki/Howard_Dean#Iowa_results_and_the_.22Scream_Heard_.27Round_the_World.22
  [your site is down, probably will never visit again. nice knowing
  you]: /2006/08/27/official-pricetrackr-launch/#comment-19
  [posted]: /2006/08/27/official-pricetrackr-launch/#comment-29
  [pear's Cache\_Lite]: http://pear.php.net/package/Cache_Lite
  [Bryce Boe Traffic Graph]: /wordpress/wp-content/uploads/2006/09/2006-bbdigggraph.png
  [priceTrackr Traffic Graph]: /wordpress/wp-content/uploads/2006/09/2006-ptdigggraph.png
  [Google Adsense]: https://google.com/adsense/
  [priceTrackr project page]: /projects/pricetrackr/
