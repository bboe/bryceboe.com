Title: Django
Date: 2007-04-22 15:27
Category: all
Tags: python
Slug: django

What two posts within an hour? Yeah I originally had this following my
previous one however the post was too long and I've decided my posts
should try to stick to a single topic.

So whilst I was waiting for Ubuntu Fesity Fawn to download I started
checking out the [Django Project][] and wow I'm pretty impressed. For my
next CS162 \`project\` we have to learn a new language or API and do a
thorough report on it. From what I've read and watched the Django
project is amazing. It's very comparable to Ruby on Rails, though I
cannot speak from experience about that.

I've already begun to create a list of strong points and weak points on
the application. By the way I'm working off the version in the SVN
trunk, but I haven't looked at the branches to see if any of these weak
points are being resolved.

First and foremost the ease of abstracting the database is by far one of
its strong points and allows developers to concentrate on their Object
Oriented (OO) programming and not worry about relationships between
object fields and database entries. With my php projects I almost never
used OO programming, as it really didn't fit my development model for
projects. The downside was that it was much slower to do it this way,
but with Django everything needs to be an object and it's great.

Along with the benefit of the previous Django has a huge downside. Once
a module is initially created and data is populated, manual table
changes are required to add or remove fields from an object. I see this
as a huge drawback because I am code by writing a few lines, testing,
and repeating. If I discover later that I need to store an additional
field I shouldn't have to manually add the field to the database but
rather it should insert a default value into the field and I should
manually add the information I need. Adding one piece of information to
x number of rows is much simpler than repopulating all the data in all
the rows. Of course there are ways I could get around this to make
adding fields simpler, however the fact still remains that I should
never have to manually change anything in the database.

Another wonderful part of Django is its admin interface. The Django
developers did all Django users a great favor by including this, because
that's typically the one part of a project I hate doing most; in fact I
usually just administer information through phpMyAdmin to avoid writing
an admin interface. Of course this is the worst way possible when
relationships need to be created.

That's really all I have currently on the subject as I haven't created a
font end to an application. My observation about it abstracting the
database is great for someone who doesn't know SQL however it also can
be seen as a bad thing. I learned sql so that I could be more efficient
with web developing by utilizing MySql to store information. Had I
started with Django and its abstraction I wouldn't be forces to
understand what's happening under the covers and thus would be stuck
when trying to troubleshoot a problem.

Thus I recommend Django to all new web developers however I also
recommend to create a really simple application with object relations,
and then create the same project using php (or in python using
python-mysql) so that one may learn what's going on under the covers,
and so that they may fully appreciate the Django project.

  [Django Project]: http://www.djangoproject.com/
