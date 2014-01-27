Title: Bye Bye Facebook: A Guide to Leaving Facebook
Date: 2010-05-13 01:34
Category: all
Tags: facebook, google, hacking, mac, python
Slug: bye-bye-facebook-a-guide-to-leaving-facebook

<ins>
Update 2010/05/27: I've made further updates to photograbber. Read about them
in my post titled, "[Facebook Photograbber Updates][]". The patch file linked
to from this page has been updated to include those changes.</ins>

I started using [Facebook][] in October of 2004, during my freshmen year of
college, just a few months after it became available at UCSB ([June 24][]). To
sign up I was required to have an email ending in @ucsb.edu and once signed up
I could easily communicate with people at UCSB, and more specifically people in
my courses; a useful feature they [later removed][]. Eventually I had the
ability to post and tag photos and well as create events to which I could
easily invite all my friends. Life was simple and so was Facebook.

Over time, Facebook expanded to allow anyone with an email address to sign up.
While I initially didn't like that just anyone could join our exclusive college
website, I gained the ability to easily keep in contact with a few more people
thus I was happy with that feature. However, when Facebook released their
[developer API][], I was initially happy, though soon later I was sorely
disappointed with the way Facebook provided third-parties with my information.
Primarily I had always wanted a way to make myself appear non-existent to
third-party applications, except for those I explicitly allowed. This is a
feature that now appears utterly unobtainable.

These last few weeks Facebook has been hot news with respect to their dishing
out of users' information to [Microsoft][], [Pandora][], and [yelp][]. Their
information whoring has prompted Minnesota's Senator, [Al Franken][], to
[include instructions on his website][] detailing how to restrict the
information flow. Wired's article, "[Facebook's Gone Rogue; It's Time for an
Open Alternative][]" pretty much covers many of the recent issues.

Thus, like many other Facebook users, the recent changes included [the straw
that broke the camel's back][] and therefore I am prepared to leave Facebook
behind for good. However, before doing so there are a few tasks that I wanted
to accomplish prior to leaving. These tasks are as follows:

1.  Obtain a copy of all the albums I am tagged in
2.  Import my Facebook contacts' emails into my Google contacts
3.  Import my Facebook contacts' profile pictures into my Google contacts
4.  Import my Facebook contacts' birthdays into my Google contacts

At this point I have accomplished all these tasks, thus while I now can leave
Facebook, there are a few precautionary things I'd like to do before finally
clicking that [delete button][] such as removing image tags and posting a [link
to this blog posting][]. Below I will detail the steps to accomplish the tasks
I have outlined.

### Obtain a copy of all the albums I am tagged in

Quite plainly there are two primary routes, which I think are good. The first
involves a Firefox extension, [facePAD][], and the second involves a desktop
application, [photograbber][].

FacePAD simply will allow you to right click on an album link and download all
of its images to your download directory. The two drawbacks to this approach
are that it's not automated, and if you want to group pictures into folders by
albums, you'll have to first manually create the folders, and second move all
the downloaded pictures into that folder. On the upside, this is a great way to
quickly download a few albums, and it'll download any picture that is viewable
by you.

![facePAD Usage][]

The other approach is using the opensource desktop application Photograbber.
Photograbber is written in python thus allowing it to run on Windows, OS X, and
Linux. As of today, photograbber is at [revision 38][], which only allows you
to download the pictures that you are tagged in, or the pictures that a
particular friend is in. These pictures are all downloaded into the same
directory and thus to me is somewhat worthless.

Fortunately, because photograbber is open source, and it was written in python
I fairly quickly was able to hack together modifications to photograbber that
allow it to accomplish precisely what I want. Which is, downloading albums that
I am tagged in where photos in each album are grouped into their own folder. I
have made available my [patch][] to photograbber which you can use to patch the
source and run yourself. Alternatively, I have also repackaged photograbber for
Mac so you don't have to mess with patching the application ([download][]).
<del>A window's repackage will follow shortly.</del> Running the application is
pretty simple, but if you need any assistance please post a comment.
<ins datetime="2010-05-14T07:22:29+00:00">I have now made a [zip file][]
available which should work on windows. Unzip, and run pg.exe. </ins>

While photograbber is fully automated once started, it does have a few
drawbacks. The first drawback is that it has a more restricted view of pictures
than what you see when you browse Facebook manually. This is because your both
you and your friends can restrict applications from having access to your photo
albums, thus to get 100% coverage of all the albums you are tagged in, you'll
unfortunately have to manually check to see what albums were downloaded and
compare that to all the albums you appear in. Additionally pictures cannot be
organized by date (I haven't checked the EXIF data), which I think is an
important feature. I'll probably add in this feature sometime before I actually
delete my account, so check back for updates.

### Import my Facebook contacts' emails into my Google contacts

I didn't find a direct way to solve this problem, though I'll admit I didn't
look very hard as I stopped with the [first result][] I found for "export
facebook emails to gmail". The method suggested involves using a Yahoo email
account. From Yahoo's contact page you can select "Tools" followed by
"Import..." and finally you have the option to import from Facebook. This uses
Facebook Connect, so you will have to authorize Yahoo to access your
information. Following the import you can select "Export..." from the "Tools"
menu and export to a "Yahoo! CSV" file, which you download to your computer.
Finally, on the Gmail contact page you can select "Import" from the upper right
and provide it with the downloaded CSV file.

### Import my Facebook contacts' profile pictures into my Google contacts

This may not be essential for many people. I wanted to accomplish this so that
all of my contacts on my Android Device have pictures next to them. For this
step I used [phaceboogle][]. At first I thought this web service was a little
sketchy, however it uses both [Facebook Connect][], and [Google's OAuth][] thus
I was cool with using it. Phaceboggle did almost exactly what I wanted, though
rather than copying the thumbnail picture, phaceboogle copied the un-cropped
profile picture, which in some cases appears with the wrong aspect ratio.
Nevertheless, I was satisfied and thus completing another step.

### Import my Facebook contacts' birthdays into my Google contacts

In order to accomplish this task as I describe, you will need an Android Device
as it utilizes the Android application, ebobirthday. This app connects to
Facebook via the Facebook API and copies over all the birthdates for your
contacts. The next time your phone syncs to your Google account, many of your
contacts will have their birthdate field completed. Now you can add a birthday
calendar to your Google Calendar ([See section 'More'][]). Task completed!

Well that's all. Feel free to post alternative methods to accomplish these
tasks, or other tasks, in the comments. Bye bye Facebook!

  [Facebook Photograbber Updates]: /2010/05/27/facebook-photograbber-updates/
  [Facebook]: http://www.facebook.com/
  [June 24]: http://web.archive.org/web/20040624152328/http://thefacebook.com/
  [later removed]: http://blog.facebook.com/blog.php?post=4314497130
  [developer API]: http://developers.facebook.com/
  [Microsoft]: http://www.microsoft.com
  [Pandora]: http://www.pandora.com/
  [yelp]: http://www.yelp.com/
  [Al Franken]: http://en.wikipedia.org/wiki/Al_Franken
  [include instructions on his website]: http://franken.senate.gov/press/?page=news_single&news_item=Facebook_Privacy_Instructions
  [Facebook's Gone Rogue; It's Time for an Open Alternative]: http://www.wired.com/epicenter/2010/05/facebook-rogue/
  [the straw that broke the camel's back]: http://en.wikipedia.org/wiki/The_last_straw
  [delete button]: http://www.facebook.com/help/contact.php?show_form=delete_account
  [link to this blog posting]: /2010/05/13/bye-bye-facebook-a-guide-to-leaving-facebook/
  [facePAD]: https://addons.mozilla.org/en-US/firefox/addon/8442/
  [photograbber]: http://code.google.com/p/photograbber/
  [facePAD Usage]: /images/2010/05/facepad.jpg "facePAD Usage"
  [revision 38]: http://code.google.com/p/photograbber/source/detail?r=38
  [patch]: http://cs.ucsb.edu/~bboe/public/patches/photograbber-r38+bboe.patch
  [download]: http://cs.ucsb.edu/~bboe/public/bin/PhotoGrabber-OSX-r38+bboe.zip
  [zip file]: http://cs.ucsb.edu/~bboe/public/bin/PhotoGrabber-WIN-r38+bboe.zip
  [first result]: http://www.google.com/support/forum/p/gmail/thread?tid=058dc912c433f1b8&hl=en
  [phaceboogle]: http://phaceboogle.bisounours.net/
  [Facebook Connect]: http://developers.facebook.com/blog/post/108
  [Google's OAuth]: http://code.google.com/apis/accounts/docs/OAuth.html
  [See section 'More']: http://www.google.com/support/calendar/bin/answer.py?hl=en&answer=37098
