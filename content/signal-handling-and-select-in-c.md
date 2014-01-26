Title: Signal Handling and Select in C
Date: 2007-09-02 18:26
Category: all
Tags: C
Slug: signal-handling-and-select-in-c

Two weeks ago I started a journey to read a textbook cover to cover so
that I'll be ready for the research I will be assisting with. Since I
have yet to take a networking class I am a bit behind where I need to
be, but that's not a problem as I learn rather quickly and Networking is
my area of interest. The book I'm reading is [Computer Networking: A
Top-Down Approach Featuring the Internet][] by [James F. Kuross][] and
[Keith W. Ross][]. I just completed the section on IP's application
layer and am familiarizing myself with socket programming in C; which I
must say is far more complicated than in python. But that's why I like
C; I get a better understanding of what is going on, and I have more
control over the sockets themselves.

My freshmen year of college [Adam][] and I wrote an IRC based protocol
and coded a server and client in Java which we called gauchoShare. I
have also written some client server programs in python but I have never
done anything in C which is what I will most likely be working with
since we are manipulating the transport layer. To give me a brief
overview of C TCP/IP sockets I read [The Pocket Guide to TCP/IP
Sockets][]. In addition to learning how to use sockets in C I also
discovered how Multiplexing input and output (I/O) works, and finally
how to use signals. As I do with most things when I learn them I create
a very simple program to demonstrate and that is what the following is.
The program when compiled will echo everything typed after *enter* has
been pressed. When closing the program via ctrl+c it will print the
message "Exit!".

~~~~ {lang="C" line="1"}
#include   // printf
#include   // FD_ functions
#include  // sig functions
#include  // exit
#include  // STDIN_FILENO

void exit_error(char* msg) {
  perror(msg);
  exit(1);
}

void KBInterrupt(int sig) {
  printf("Exit!\n");
  exit(1);
}

int main() {
  // Variables
  fd_set fd;
  int charsRead;
  char buff[256];
  struct sigaction handler;

  // Setup Action Handler
  handler.sa_handler = KBInterrupt; // Function to call
  if (sigfillset(&handler.sa_mask) < 0)
    exit_error("sigfillset failed");
  handler.sa_flags=0;
  if (sigaction(SIGINT,&handler,0) < 0) // Setup signal
    exit_error("sigaction failed");

  // Setup file descriptors
  FD_ZERO(&fd);
  FD_SET(STDIN_FILENO,&fd);

  // The main part of the program
  for (;;) {
    select(STDIN_FILENO+1,&fd,NULL,NULL,NULL);
    if(FD_ISSET(STDIN_FILENO,&fd)) { // Checks if enter has been pressed
      charsRead = read(STDIN_FILENO,buff,255);
      write(STDOUT_FILENO,buff,charsRead);
    }
  }
  return 0;
}
~~~~

When Adam and I wrote gauchoShare in Java we were not aware of I/O
multiplexing and thus we created a new thread to handle keyboard input
from the user. This obviously has increased overhead, and multiplexing
easily solves that problem. In addition to multiplexing the program
demonstrates how to handle the interrupt signal sent by ctrl+c in linux.

  [Computer Networking: A Top-Down Approach Featuring the Internet]: http://www.amazon.com/Computer-Networking-Top-Down-Approach-Featuring/dp/0321227352/ref=sr_11_1/102-4260619-0027306?ie=UTF8&qid=1188781467&sr=11-1
  [James F. Kuross]: http://www-net.cs.umass.edu/personnel/kurose.html
  [Keith W. Ross]: http://cis.poly.edu/~ross/
  [Adam]: http://www.adamdoupe.com
  [The Pocket Guide to TCP/IP Sockets]: http://www.amazon.com/Pocket-Sockets-Version-Kaufmann-Practical/dp/1558606866/ref=sr_11_1/102-4260619-0027306?ie=UTF8&qid=1188781976&sr=11-1
