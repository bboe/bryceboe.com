Title: My smb.conf
Date: 2007-07-11 00:29
Category: all
Slug: my-smbconf

This is about the 5th time I had to redo our smb.conf for our file server in
the hallway. I'm not very good at making backups of that machine when we
upgrade the hardware or software, and there really is no reason to except for
this one file. Well I think I've finally mastered it, and I want to put it in a
location where I'll be able to find it for future resources.

    [global]
       workgroup = MSHOME
       server string = %h server (Samba, Ubuntu)
       dns proxy = no
       log file = /var/log/samba/log.%m
       max log size = 1000
       syslog = 0
       panic action = /usr/share/samba/panic-action %d
       encrypt passwords = true
       passdb backend = tdbsam
       obey pam restrictions = yes
       invalid users = root
       printcap name = /dev/null
       map to guest = Bad User

    [homes]
       browseable = no
       valid users = %S
       read only = no
       create mask = 0664
       directory mask = 0775

    [Programs]
       path = /home2/Programs
       guest ok = yes
       read only = yes
       force group = +trigo
       write list = @trigo
       create mask = 0664
       directory mask = 0775

We have more shares but from the Programs share I know I'll be able to figure
out the rest and hopefully you can figure it out too.

A quick run down:

-   printcap name = /dev/null -- We don't care about printer settings and it
    seems the logs are flooded with messages about printers if this line isn't
    there
-   map to guest = Bad User -- This allows guest users even though the security
    setting is set to user (by default)
-   [homes] -- this is setup so that only the proper user can access their
    share via smb.
-   [Programs] -- guest ok must be specified for the guest account to access
    the folder. read only ensures that guest accounts cannot write. The force
    group option with the plus (+) indicates that if the user belongs to the
    group trigo then any file/folder created will have that group specified as
    its owner. The option write list when used with the at (@) sign indicates
    that any members of the trigo group has write permission to the share.
    Finally the masks ensure that the group has proper edit/delete privileges
    to files/folders created through smb.

This setup is ideal since the three of us wish to have read/write access to our
files while only granting others read access.

Completely separately from my very limited experimentation it seems NFS is at
least five times faster, transferring a single large file (such as an Ubuntu
ISO) than is SMB. The only problem is it is basically infinitely less secure
than SMB because it doesn't require any form of authentication. This just poses
the question of which is more important, speed or security?
