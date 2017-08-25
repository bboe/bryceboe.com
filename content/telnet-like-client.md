Title: Telnet-like client
Date: 2007-09-22 10:17
Category: all
Tags: C
Slug: telnet-like-client

Using the methods I discussed previously I wrote a telnet-like client which can
be used to communicate with any type of text based server such as mail and web
servers. The following isn't 100% perfect as it doesn't handle early returns
from [send][] as I wasn't able to properly test this behavior.

    #include <stdio.h>  // perror,printf
    #include <stdlib.h> // exit
    #include <string.h> // strerror
    #include <netdb.h>  // gethostbyname
    #include <sys/socket.h>
    #include <fcntl.h>  // FD_ functions
    #include <signal.h> // sig functions
    #include <unistd.h> // STDIN_FILENO

    int client_socket;

    void exit_error(char* msg) {
      perror(msg);
      exit(1);
    }

    void exit_close(char* msg) {
      close(client_socket);
      exit_error(msg);
    }

    void KBInterrupt(int sig) {
      close(client_socket);
      exit(0);
    }

    int main(int argc, char* argv[]) {
      /* Variables */
      struct hostent *server_host;
      struct sockaddr_in server_addr;
      fd_set fd;
      int charsRead, charsWritten;
      int char_buff_size = 1024;
      char char_buffer[char_buff_size];
      struct sigaction handler;

      /* Verify arguments */
      if (argc < 3) {
        fprintf(stderr,"usage %s hostname port\n",argv[0]);
        exit(0);
      }

      /* Setup Action Handler */
      handler.sa_handler = KBInterrupt;
      if (sigfillset(&handler.sa_mask) < 0)
        exit_error("sigfillset failed");
      handler.sa_flags = 0;
      if (sigaction(SIGINT,&handler,0) < 0)
        exit_error("sigaction failed");

      /* Create TCP socket */
      if((client_socket = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP)) < 0)
        exit_error("Could not create socket");

      /* Get host information. This takes a fqdn or IP address */
      if ((server_host = gethostbyname(argv[1])) == NULL) {
        herror(argv[1]);
        exit(1);
      }

      /* Setup and fill in values for server_addr */
      bzero((char*)&server_addr,sizeof(server_addr));
      server_addr.sin_family = server_host->h_addrtype;
      bcopy((char*)server_host->h_addr,
        (char*)&server_addr.sin_addr.s_addr,
        server_host->h_length);
      server_addr.sin_port = htons(atoi(argv[2]));

      /* Connect */
      if (connect(client_socket,(struct sockaddr*)&server_addr,sizeof(server_addr)) < 0)
        exit_error("ERROR connecting");

      /* The Main part of the program */
      for(;;) {
        /* Setup file descriptors */
        FD_ZERO(&fd);
        FD_SET(STDIN_FILENO,&fd);
        FD_SET(client_socket,&fd);

        /* Wait for input via keyboard or socket */
        select(client_socket+1,&fd,NULL,NULL,NULL);
        if(FD_ISSET(STDIN_FILENO,&fd)) { /* Keyboard input */
          if ((charsRead = read(STDIN_FILENO,char_buffer,char_buff_size)) < 0)
        exit_close("ERROR reading from STDIN");
          if ((charsWritten = send(client_socket,char_buffer,charsRead,0)) != charsRead)
          exit_close("Did not write enough\n");
        }
        if(FD_ISSET(client_socket,&fd)) { /* Socket input */
          if ((charsRead = recv(client_socket,char_buffer,char_buff_size,0)) < 0)
        exit_close("ERROR reading from socket");
          else if (charsRead == 0)
        exit_close("Connection closed");

          /* Output to screen */
          charsWritten = 0;
          int temp = 0;
          while ((temp = write(STDOUT_FILENO,&char_buffer[charsWritten],charsRead-charsWritten)) > 0)
        charsWritten += temp;
          if (temp < 0)
          exit_close("ERROR writing to screen");
        }
      }

      /* Unreachable */
      return 0;
    }

Pretty simple.

  [send]: http://www.opengroup.org/onlinepubs/009695399/functions/send.html
