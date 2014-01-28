Title: Moving Images in 3D Space with Pyglet
Date: 2011-10-08 16:04
Category: all
Tags: python, visualization
Slug: moving-images-in-3d-space-with-pyglet

Yesterday, October 7, 2011, the graduate students of UCSB's Computer Science
department, including myself, hosted the [6th annual Graduate Student Workshop
on Computing (GSWC)][]. The workshop is a great opportunity for other students,
faculty, and industry professionals to get an overview of the work performed by
our department. Part of organizing the workshop is obtaining gift or
sponsorship money in order to pay for the facilities, food, proceedings, and
all other costs associated with running a workshop.

In exchange for event sponsorship, we include each company's logo on our
website, in the conference proceedings, and in a visible display at the
workshop itself. For many of the previous GSWCs, we created and printed up an
expensive poster with the theme of the event as well as logos of all the
corporate sponsors. While that worked well, it required a decent effort to
design the poster, and, as I said before, was considerably expensive to print.
Thus, when I was the chair of the GSWC last year, I decided to take a different
approach to how we display the corporate logos during the workshop. Rather than
using a static poster, I created an animated display that was projected on one
of the room's walls during the conference.

I occasionally provide consulting for a local Santa Barbara company,
[Worldviz][] who makes a product, [Vizard][], that allows one to quickly
construct 3D environments in python. Using Vizard I was able to quickly create
a 3D logo display in which the logos follow a circular path along the z-axis,
as shown in the following photos. While this worked well, Vizard unfortunately
only works on Windows and thus could not be run easily from my Mac laptop.

[![image][]](/images/2011/10/animator0.png)
[![image][1]](/images/2011/10/animator1.png)
[![image][2]](/images/2011/10/animator2.png)
[![image][3]](/images/2011/10/animator4.png)

We wanted to use the same display for this year's GSWC so I sought to rewrite
the display in a cross platform and free manor. While I have some previous
opengl experience in C, I really wanted to write the display in python so I
looked at the various python opengl options. From the StackOverflow thread,
[OpenGL with Python][], I quickly settled on [pyglet][]. Since I already knew
the equation to move points around in a circular path, my only challenge was to
figure out how to map a texture to a quad so that I could position the quad in
3D space. I quickly asked a StackOverflow question, [Moving an image around in
3D space][] in hopes that while I was in the process of figuring it out,
someone would provide me with the solution. Unfortunately, [crowdsourcing][]
didn't pay off, nevertheless, I eventually found the solution and wrote a
simple cross platform logo animation program.

In order to run the following program, you will first need to install the
required libraries (an exercise left to the reader), create a folder "imgs" and
place whatever images you want in that folder and then run the following script
([download animator.py][]). Note: If you want to run this script on 64-bit OS X
you'll need to run it via: `VERSIONER_PYTHON_PREFER_32_BIT=yes ./animator.py`

    #!/usr/bin/env python
    import math, os, pyglet, sys
    from pyglet.gl import *

    class World(pyglet.window.Window):
        def __init__(self, scale=10, center_pos=(0, 0, -15), speed=1.0,
                     *args, **kwargs):
            super(World, self).__init__(*args, **kwargs)
            self.scale = scale
            self.center_pos = center_pos
            self.speed = speed
            glClearColor(1.0, 1.0, 1.0, 0.0)
            glEnable(GL_DEPTH_TEST)
            self.textures = self.load_textures()
            self.clock = 0
            pyglet.clock.schedule_interval(self.update, 1 / 60.0)

        @staticmethod
        def load_textures():
            img_dir = 'imgs'
            textures = []
            if not os.path.isdir(img_dir):
                print 'Could not find directory "%s" under "%s"' % (img_dir,
                                                                    os.getcwd())
                sys.exit(1)
            for image in os.listdir(img_dir):
                try:
                    image = pyglet.image.load(os.path.join(img_dir, image))
                except pyglet.image.codecs.dds.DDSException:
                    print '"%s" is not a valid image file' % image
                    continue
                textures.append(image.get_texture())

                glEnable(textures[-1].target)
                glBindTexture(textures[-1].target, textures[-1].id)
                glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height,
                             0, GL_RGBA, GL_UNSIGNED_BYTE,
                             image.get_image_data().get_data('RGBA',
                                                             image.width * 4))
            if len(textures) == 0:
                print 'Found no textures to load. Exiting'
                sys.exit(0)
            return textures

        def update(self, _):
            self.on_draw()
            self.clock += .01

        def on_draw(self):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            self.draw_images()

        def draw_images(self):
            angle_base = (self.clock * self.speed * 50) % 360
            angle_delta = 360. / len(self.textures)

            for i, texture in enumerate(self.textures):
                angle = math.radians((angle_base + i * angle_delta) % 360)
                dx = math.sin(angle) * self.scale
                dz = math.cos(angle) * self.scale

                if texture.width > texture.height:
                    rect_w = texture.width / float(texture.height)
                    rect_h = 1
                else:
                    rect_w = 1
                    rect_h = texture.height / float(texture.width)

                glPushMatrix()
                glTranslatef(dx + self.center_pos[0], self.center_pos[1],
                             dz + self.center_pos[2])
                glBindTexture(texture.target, texture.id)
                glBegin(GL_QUADS)
                glTexCoord2f(0.0, 0.0); glVertex3f(-rect_w, -rect_h, 0.0)
                glTexCoord2f(1.0, 0.0); glVertex3f( rect_w, -rect_h, 0.0)
                glTexCoord2f(1.0, 1.0); glVertex3f( rect_w,  rect_h, 0.0)
                glTexCoord2f(0.0, 1.0); glVertex3f(-rect_w,  rect_h, 0.0)
                glEnd()
                glPopMatrix()

        def on_resize(self, width, height):
            glViewport(0, 0, width, height)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(65.0, width / float(height), 0.1, 1000.0)
            glMatrixMode(GL_MODELVIEW)


    if __name__ == "__main__":
        window = World(width=800, height=600)
        pyglet.app.run()

  [6th annual Graduate Student Workshop on Computing (GSWC)]: http://gswc.cs.ucsb.edu/2011/
  [Worldviz]: http://www.worldviz.com/
  [Vizard]: http://www.worldviz.com/products/vizard4/index.html
  [image]: /images/2011/10/animator0-150x150.png "animator0"
  [1]: /images/2011/10/animator1-150x150.png "animator1"
  [2]: /images/2011/10/animator2-150x150.png "animator2"
  [3]: /images/2011/10/animator4-150x150.png "animator4"
  [OpenGL with Python]: http://stackoverflow.com/questions/242059/opengl-with-python
  [pyglet]: http://pyglet.org/
  [Moving an image around in 3D space]: http://stackoverflow.com/questions/7681899/moving-an-image-around-in-3d-space
  [crowdsourcing]: http://en.wikipedia.org/wiki/Crowdsourcing
  [download animator.py]: /images/2011/10/animator.py
