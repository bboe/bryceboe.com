Title: Tethering OS X Lion to Android
Date: 2011-10-20 14:24
Category: all
Tags: mac
Slug: tethering-os-x-lion-to-android

I'm currently in Chicago, having just attended the [18th ACM Conference on
Computer and Communications Security][], where [Adam Doupé][] presented our
paper, [Fear the EAR: Discovering and Mitigating Execution After Redirect
Vulnerabilities][]. As always, when I'm traveling, the problem of how to
connect to the Internet arises. Fortunately, we were provided with Internet
access via WiFi in our rooms throughout the duration of the conference,
however, now that the conference is over we'll have to pay for the access
ourselves. Hotels, like many airports, charge absurd amounts for Internet
access simply because they can. $8 a day for an *unreliable* and *slow*
connection is typical and is *absurd* considering I'm already paying $30 a
month for an unlimited data plan on my cell phone. Of course I can check my
email, read [reddit][], and maybe look up some places on [yelp][] using my
Android phone, however, it is simply more efficient to use my laptop.

Naturally, the obvious solution is to tether your laptop to your phone and if
you have an Android phone the process is incredibly simple. In fact, there are
a number of pages on the Internet that tell you exactly how to do it.
Primarily, there is an [Android Forums post][] from November, 2009 that
recommends using an Android application, [Azilink][], in combination with an OS
X application [Tunnelblick][], and a [shell script][] to configure the tether
correctly. There is also a [great blog post][] from March of this year that is
a bit more user friendly than the forum post in describing how to tether your
OS X machine to your Android phone.

Despite the last guide being fairly recent, it unfortunately is slightly out of
date due in part to OS X Lion. The older versions of Tunnelblick seemingly
don't work with OS X Lion, thus an update to a newer version of Tunnelblick is
required. The newer version (currently 3.2beta32) of Tunnelblick breaks the
shell script that the previous guide uses, thus I am writing this post simply
to provide the Internet with an update to that shell script. Please note that
everything else mentioned on the blog post currently works as described.

The fix to the shell script is actually really simple, just replace the line
shown in the first block of code below, with the line shown in the second:

`sudo /Applications/Tunnelblick.app/Contents/Resources/openvpn --dev tun \    sudo /Applications/Tunnelblick.app/Contents/Resources/openvpn/openvpn-2.2.1/openvpn --dev tun \`

Finally for your convenience, I created a github gist with the updated shell
script. Observant readers will notice that I updated some of the comments in
the script. Happy tethering!

[gist id=1302227]

  [18th ACM Conference on Computer and Communications Security]: http://www.sigsac.org/ccs/CCS2011/
  [Adam Doupé]: http://adamdoupe.com/
  [Fear the EAR: Discovering and Mitigating Execution After Redirect
  Vulnerabilities]: http://cs.ucsb.edu/~bboe/public/pubs/fear-the-ear-ccs2011.pdf
  [reddit]: http://reddit.com
  [yelp]: http://yelp.com
  [Android Forums post]: http://androidforums.com/droid-how-tips/18532-mac-os-x-droid-tethering-usb-wired.html
  [Azilink]: http://code.google.com/p/azilink/
  [Tunnelblick]: http://code.google.com/p/tunnelblick/
  [shell script]: http://pastie.org/701122
  [great blog post]: http://mornin.org/blog/howto-tether-android-phone-mac-os-x/
