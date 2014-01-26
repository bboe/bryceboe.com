Title: Recap: Fall 2007
Date: 2007-12-13 17:56
Category: all
Slug: recap-fall-2007

Another quarter has passed at UCSB as I just finished my last final
about two hours ago. Overall this was quite an interesting quarter in
which I started off taking three classes: Intro to Networking, Computer
Graphics and a special class to prepare for the ACM Programming
Competition. In addition to this classes I signed up for Master's
research under [Ben Zhao][], a fantastic professor, and a few weeks into
the quarter I added a graduate class on writing and presentations. The
writing and presentation class was one of the most amazing nontechnical
courses I've taken at UCSB. I gained experience presenting as well as
some tips to improve my presentation. While I continue to feel I
struggle with writing, I've discovered my main problem is not wanting to
put the effort into it, and when I put in the effort it shows.

To prepare for my networking research I was given a networking book
which I read a large portion of prior to the start of the quarter. As it
turned out, this was the same book used in the intro to networking class
and thus I was two months ahead of the class. Despite the repeat in
material it was an amazing class with an [awesome Professor][]; I can
only hope the other networking classes I take will be as exciting. With
my reading and through the course I can confidently say that I know
nearly 100% of all actions that occur between two communicating nodes on
the internet. Of course we didn't cover every internet protocol, but
nonetheless I'm a networking baller.

Since I work for a Computer Graphics Comanpy, [WorldViz][], I signed up
for the computer graphics class. I wanted to get a better idea of how
OpenGL and scene graphs work as they, along with our program
([Vizard][]), make everything so simple. Unfortunately the class was
taught by a Professor which I seemingly cannot learn from, and given my
chats with other students, I'm not the only one. Thus, I was forced to
learn everything on my own. My primary problem with the Professor is his
lecture style in which a single lecture may cover up to 80 slides of
which he jumps back and forth between making it very difficult to
follow. I'm not an expert on teaching, however I know he is doing
something wrong as in a class of about twenty students only five would
attend the lectures. In a CS class one should expect just over half the
class to attend, but not a quarter. My gripes aside, with the studying I
did for the final, I finally learned some of the concepts I wish to
leave the quarter with which were matrix transformations and
projections. I just wish I didn't have to learn it on my own.

The ACM preparation course was awesome as there were only six of us in
the class with [one of the coolest Professors on campus][], along with
the other two previously mentioned. We covered some advanced algorithms
needed for solving programming competition problems. As I mentioned in a
previous post, Adam, Scott and myself placed 5th last year at the
competition without any formal preparation, thus we were expecting to be
much more prepared this year. Unfortunately despite all the preparation,
luck is also a factor in the competition, and unfortunately I think luck
was why we did so well the year before. This year we placed 12th only
managing to solve three problems. In comparison last year we manged to
solve five problems. My explanation for the decline is in the previous
year two of the problems I solved were dynamic programming problems, my
forte, of which none of the problems this year were. Nonetheless it was
fun and we'll get to have another go at it next year.

On the research front I've been working on vulnerabilities in transport
layer protocols. I wont go into detail, however I will say research has
been fun, but [NS-2][], the network simulator tool, is horrible. It
interfaces with the [TCL][] scripting language which I think was a
terrible choice as TCL has the worst error reporting mechanism I've
seen. I've silently been planning to re-implement NS-2 using [python][],
however it doesn't seem worth it as I'm hoping to not have to use NS-2
much after this project.

On the project front I had time for one project of my own and completed
some pretty cool projects for my classes. My own project I call Simple
File Transfer which I designed a protocol similar to TFTP and FTP. Like
TFTP there is a very limited number of commands, GET, PUT and QUIT,
however unlike TFTP it uses TCP to send data. Finally unlike FTP it
sends data in band which means the data and control signals are sent
through the same connection in the same way HTTP data is sent in band.
For my graphics class we had to program a cube animation sequence which
included textures and shadows as well as a separate program on
generating Bezier curves. The networking projects were all simpler than
my Simple File Transfer and thus deserve no mention except for the extra
credit assignment in which we were to code up a proxy server. I chose to
do this assignment in python and the resulting code, with some extras,
was only 107 lines; Python is awesome as demonstrated by [this][] XKCD
comic, though I've known it for far longer than the comic author.

Well I think I'll wrap it up now as this has been a pretty long post. In
the words of [Ron Burgandy][], "You stay classy [the one or two readers
I have]." By the way if you do actually read this how about some
comments which spark discussion, or just comments? If you want to be
anonymous just use a fake name and a fake email address and assuming
it's a non-spam comment I'll accept it.

  [Ben Zhao]: http://cs.ucsb.edu/~ravenben/
  [awesome Professor]: http://cs.ucsb.edu/~ebelding/
  [WorldViz]: http://www.worldviz.com/
  [Vizard]: http://www.worldviz.com/products/vizard/index.html
  [one of the coolest Professors on campus]: http://cs.ucsb.edu/~sherwood/
  [NS-2]: http://www.isi.edu/nsnam/ns/
  [TCL]: http://www.tcl.tk/
  [python]: http://www.python.org/
  [this]: http://www.xkcd.com/353/
  [Ron Burgandy]: http://en.wikipedia.org/wiki/Anchorman:_The_Legend_of_Ron_Burgundy
