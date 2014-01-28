Title: Bypassing Gogo's Inflight Internet Authentication
Date: 2012-03-12 17:19
Category: all
Slug: bypassing-gogos-inflight-internet-authentication

Two weeks ago I attended [SIGCSE 2012][] in Raleigh, NC. The plane on my return
flight had Internet access through [Gogo's Inflight Internet][]. While I think
it's incredibly awesome that Internet access is readily available to those who
travel by plane, I personally feel it is not worth $12.95 for a few hours of
access. Nevertheless, I figured I'd simply connect to Gogo's network to see
what sort of access was permitted to non-authenticated, i.e., non-paying,
users. What I discovered surprised me: I was able to gain access to the entire
Internet.

Immediately from links on their landing page it was apparent that Gogo
permitted access to its own website, as well as the airline's website and a few
other third-party sites such as [Living Social][], and [Eventful][]. Attempting
to access any other website resulted in a redirect to Gogo's landing page. Gogo
appears to accomplish this by responding with an HTTP redirect to any standard
HTTP request, i.e., port 80, that is sent to a non-permitted IP address.

Two common techniques for bypassing pay-for-wireless providers are
[TCP-over-ICMP][] and [TCP-over-DNS][]. In a nutshell, TCP is the protocol
required to browse the web, ICMP is the protocol used by the command `ping` to
determine if a host is available, and DNS is required to resolve domain names
like [www.google.com][] to an IP address. When TCP is not completely available
yet either ICMP or DNS is, then it is possible to encapsulate TCP connections
over the other available protocol. Gogo blocked my ping attempts, hence
TCP-over-ICMP was not possible. However, while Gogo doesn't permit direct
access to external DNS servers, Gogo's DNS server recursively resolved the DNS
queries I made. Therefore, Gogo appears to be susceptible to TCP-over-DNS.
Despite not being able to verify this finding, I will simply state that Gogo
can remedy this, if necessary, by only responding to white-listed DNS queries
for non-authenticated users.

As a quick aside, I would like to mention I made an attempt to responsibly
disclose this information to Gogo prior to posting this article [[1][], [2][]].
I contacted one of their twitter representatives via email who informed me the
right person would contact me. After a few days with no response, I sent a
follow up email to the same twitter representative. While that representative
has continued to tweet since my followup, I have received no replies. Thus, I
have come to the conclusion that Gogo is uninterested. I proceed with the
knowledge that this authentication bypass in no way compromises Gogo's
security; therefore, it is of negligible importance to Gogo's existing
customers. Finally, I proceed knowing very well that Gogo's sysadmins can
correct the underlying problem in a very brief period of time and I even
present them with the solution.

♫[Now back to the good part][]!♫

I use [Google Chrome][] as my primary browser and along with it I have
installed a few extensions that depend on connections to various Google
services. When Chrome is open and does not have a connection to the Internet,
some of these extensions, such as the [Google Reader Notifier][], adjust their
icon to indicate their disconnected status. As expected, the Google Reader
Notifier extension indicated that I was not connected to the Internet. However,
as I was browsing around Gogo's landing page and permitted sites, I was shocked
when the [Google Voice][] extension notified me of a new text message and
shocked again when I successfully replied. I had mistakenly stumbled across a
hole in Gogo's access policies and decided to dig deeper.

As I previously mentioned, Gogo redirected to their landing page upon any
standard HTTP request. However, the same was not true for HTTPS connections,
which by default occur on TCP port 443. Thus, for some unknown reason, my
computer was able to connect to [www.google.com][] via HTTPS. Immediately I
tried other Google services, like [mail.google.com][] for Gmail, and
[docs.google.com][] for Google docs; neither worked. Nevertheless, any Google
service accessible via HTTPS and addressed under the [www.google.com][] domain
worked flawlessly.

After poking around to find a list of Google services meeting these
requirements, I had an epiphany. While I probably learned this information at
some point in my past, I had a hunch that Google's front-end web servers would
likely provide the correct response to any Google web service. Hence, I opened
up my /etc/hosts file on my OS X machine, and added the following line:

    :::text
    74.125.225.40 mail.google.com

Voila! Immediately, I was able to access Gmail. The IP address, 74.125.225.40,
corresponds to the IP address my computer was successfully able to connect to
in order to access services under the [www.google.com][] domain. By adding this
manual entry to my hosts file, I informed my operating system to use the
provided IP address when attempting to connect to mail.google.com. In order to
additionally receive successful access to [Google+][], [YouTube][], [Google
Docs][docs.google.com], [Google Code][], and Google's chat interface, I updated
the line to the following:

    :::text
    74.125.225.40 mail.google.com plus.google.com youtube.com docs.google.com code.google.com chatenabled.mail.google.com

What I previously described is how I was able to bypass Gogo's Inflight
Internet Authentication in order to access a number of Google services for
free. What remains is how to utilize this information to access the entire
Internet. The answer to this question lies with [Google AppEngine][].

Google AppEngine (GAE) is a cloud-based web application hosting service
provided by Google. Anyone can run a GAE application on Google's servers. As I
previously described, Google's front-end web servers respond to requests for
any Google web service, including third-party GAE applications. The final piece
of the puzzle is that GAE allows its applications to themselves make web
requests. Therefore, a well written GAE application can operate as a proxy
server. In fact, there are a number of available packages for running simple
GAE proxy servers. [Digital Inspiration][] and [Windows Guides][] each provide
tutorials for setting up such proxies. The Windows Guides tutorial even links
to a working example at <https://jttm-server-prox.appspot.com/>. A user of
Gogo's Inflight Internet need only add jttm-server-prox.appspot.com to their
hosts file in order to utilize this proxy to access much of the Internet.

I have previously described how Gogo's Inflight Internet authentication can be
bypassed through the combination of a custom hosts file and a GAE proxy server.
The remainder of this article will detail how Gogo can fix this problem.

The root question, is: why does Gogo allow non-authenticated access to some
Google IPs? While my answer to this question is purely speculation, the
solution I offer will absolutely solve the problem. I speculate that Gogo
allows access to some Google IPs because of [Google Analytics][] and [Google
Adsense][], indicated in client scripts by the domains www.google-analytics.com
and ad.doubleclick.net respectively. If correct, Gogo's sysadmins simply
white-listed a few too many IP addresses. Regardless, the point is moot because
any Google front-end web server IP address, including those for Analytics and
Adsense, will serve the reply for all Google web services, most notably GAE
applications. Hence, by white-listing any single Google front-end web server IP
address, Gogo is essentially providing access to the entire Internet. It
follows, that the simplest solution to this bypass is for Gogo to completely
disable direct access to Google IPs from non-authenticated users.

While the above solution absolutely works, it prevents Gogo from tracking users
and serving ads using Google services. Of course, serving ads is pointless when
non-authenticated users cannot visit the target site of the advertisement, so
let's forget about Google Adsense. Google Analytics on the other hand, is a
useful tool for monitoring users' access to a website. Let's now proceed under
the assumption that it is essential for Gogo's non-authenticated users to have
access to whatever Google service Gogo intended to allow, and for simplicity
assume it is the Google Analytics tracking service. The question now is: how
can Gogo allow access to the Google Analytics tracking service without allowing
access to all other Google services? This answer partially lies with [Server
Name Indication][].

Server Name Indication (SNI) is implemented on most modern web browsers and
allows a web server with a single IP address to serve multiple TLS
certificates. The proper certificate is returned in response to the hostname
provided in the TLS client handshake. The use of SNI is why, despite using the
same IP address for all the aforementioned services, Google is able to return
the appropriate domain-specific TLS certificate. Therefore, Gogo can
additionally white-list on the SNI-hostname in order to prevent the
authentication bypass and still allow access to Google Analytics. However,
things are not so simple, as Google's servers do not depend on the presence of
the SNI-hostname in the TLS client handshake.

In the absence of SNI, Google's front-end web servers return the default TLS
certificate for that particular server, yet, the server still responds with the
requested content as indicated in the HTTP host header. Because the HTTP host
header is encrypted, as well as the entire response, it is not possible to
discern desired requests from undesired requests. One solution is to only allow
such access to Google Analytics if the client supports SNI and the SNI-hostname
is in the white-list. While this approach would work, it appears it would
restrict access to Google Analytics for some browsers that are [still commonly
used][].

Regardless, I suspect that Google's front-end web servers do not verify
consistency between the SNI-hostname and the HTTP host header. Under that
assumption, it would still be possible, in the presence of an SNI-hostname
white-list, to bypass Gogo's authentication with a custom browser (or local
proxy server) that negotiates TLS handshakes using only the expected
SNI-hostname yet still makes the desired Google web service request. While I
don't believe anything is readily accessible to make this process easy for
99.9% of Gogo's potential customers, it only requires a single person's
determination to make it so. Thus, the only be-all-end-all solution to prevent
this bypass is for Gogo to completely disable direct access to Google IPs from
non-authenticated users.

There is, of course, one other possible solution: Gogo could
[man-in-the-middle][] the desired Google web services in order to perform
filtering on the HTTP host header. However, this approach could have unforeseen
consequences. Therefore, I do not recommend it.

In conclusion, I have described how one can currently bypass Gogo's Inflight
Internet authentication to access much of the Internet using a custom host file
and a Google AppEngine proxy. I have also described how Gogo can somewhat block
this bypass by supplementing their IP white-list with both an SNI requirement
and an SNI-hostname white-list. Finally, I speculated that even with the
aforementioned solution, it would still be possible for a determined user to
bypass their authentication. Thus, I stated the only real solution is for Gogo
to not allow any direct access between non-authenticated users and Google web
servers.

Happy "free" surfing, for now anyway :)

  [SIGCSE 2012]: http://www.sigcse.org/sigcse2012/
  [Gogo's Inflight Internet]: http://www.gogoair.com/
  [Living Social]: livingsocial.com
  [Eventful]: http://eventful.com/
  [TCP-over-ICMP]: http://www.cs.uit.no/~daniels/PingTunnel/
  [TCP-over-DNS]: http://analogbit.com/tcp-over-dns_howto
  [www.google.com]: http://www.google.com
  [1]: /images/2012/03/gogo_dm.png
  [2]: https://twitter.com/#!/Gogo/status/176504298967015424
  [Now back to the good part]: http://www.youtube.com/watch?v=GI6CfKcMhjY&t=1m37s
  [Google Chrome]: https://www.google.com/chrome
  [Google Reader Notifier]: https://chrome.google.com/webstore/detail/apflmjolhbonpkbkooiamcnenbmbjcbf
  [Google Voice]: https://chrome.google.com/webstore/detail/kcnhkahnjcbndmmehfkdnkjomaanaooo
  [mail.google.com]: http://mail.google.com
  [docs.google.com]: http://docs.google.com
  [Google+]: http://plus.google.com
  [YouTube]: http://youtube.com
  [Google Code]: http://code.google.com
  [Google AppEngine]: http://code.google.com/appengine/
  [Digital Inspiration]: http://www.labnol.org/internet/setup-proxy-server/12890/
  [Windows Guides]: http://mintywhite.com/software-reviews/security-software/set-proxy-google-app-engine/
  [Google Analytics]: http://www.google.com/analytics/
  [Google Adsense]: https://www.google.com/adsense/
  [Server Name Indication]: http://en.wikipedia.org/wiki/Server_Name_Indication
  [still commonly used]: http://en.wikipedia.org/wiki/Server_Name_Indication#No_support
  [man-in-the-middle]: http://en.wikipedia.org/wiki/Man-in-the-middle_attack
