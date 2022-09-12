Title: Facebook Photograbber Updates
Date: 2010-05-27 11:28
Category: all
Tags: facebook, python
Slug: facebook-photograbber-updates

I [previously wrote][] about my preparation for leaving Facebook. This morning
I have finally completed the last few things I wanted to do. Those last few
things were to store the photo captions, photo comments, and photo tags for
each photo downloaded.

Yesterday, in order to extract this information from Facebook, I spent some
time and made some significant modifications to [photograbber][]. You can
download the patch [here][]. The changes are as follows:

-   GUI checkbox option to download entire album if tagged
-   Saves photo caption and comments in *{pid}*\_comments.txt
-   Saves photo tags in *{pid}*\_tags.txt
-   Photos modify time is set to the upload time of the photo
-   Comment file modify time is set to the time of the last comment
-   Tag file modify time is set to the time of the photo upload
-   Improved error and thread exit handling (not perfect though :-/)

Features specific to the complete album download feature

-   Stores pictures and metadata for an album within a folder named
    *{username}*-*{album\_name}*
-   Replaces invalid characters and spaces with underscore
-   Saves album comments in ALBUM\_COMMENTS.txt
-   Album folder modify time is set to the modify time of the the album

Photo captions and comments are stored in the following form:

    Photo Caption
    The only men running in bikini bottoms.

    Sun Sep  6 18:20:52 2009 John Smith
    high five.  a million high hives.

    Sun Sep  6 20:05:40 2009 Sally Thomson
    OH my gosh ... I love it!

Album descriptions, locations, and comments are stored in the following form:

    Album Description
    The best vacation ever!

    Album Location
    Aruba

    Tue Jul 21 15:33:46 2009 Sally Thomson
    whatever u do don't get abducted! jk ;)

    Tue Jul 21 15:35:44 2009 Bryce Boe
    I don't even know how that's possible there as everyone was so nice.

I have yet to make a Windows and OS X build, but if you're not afraid of a
terminal and have *svn*, *wget*, *patch*, and *python* you can get and run my
modified version of photograbber via:

    svn checkout http://photograbber.googlecode.com/svn/trunk/ photograbber-read-only -r38
    cd photograbber-read-only/
    wget -qO - https://bryceboe.com/public/photograbber/photograbber-r38+bboe.patch | patch -p0
    echo "Run via: python pg.py"
    python pg.py

  [previously wrote]: /2010/05/13/bye-bye-facebook-a-guide-to-leaving-facebook/
  [photograbber]: http://code.google.com/p/photograbber/
  [here]: /public/photograbber/photograbber-r38+bboe.patch
