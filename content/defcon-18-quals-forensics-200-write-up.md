Title: Defcon 18 Quals Forensics 200 Write up
Date: 2010-05-25 14:43
Category: all
Tags: hacking, python
Slug: defcon-18-quals-forensics-200-write-up

<ins>Edit: A bunch more DEFCON 18 write ups can be found at the
[vnSecurity site][].</ins>

This weekend I competed in the Defcon 18 Qualifiers with team
Shellphish. We unfortunately only placed 15th, nonetheless, it was an
exciting and challenging weekend. Below is my write up for the Forensics
200 challenge.

~~I don't recall the phrasing they gave (if you remember it please let
me know), however this was the file they provided:~~
<ins datetime="2010-05-26T03:34:43+00:00">The caption read, "find the
key" and linked to this file:</ins>
[f200\_02b7b50f575759cff7.tar.lzma][]

Running *file* on f200\_02b7b50f575759cff7.tar.lzma simply returned
**data** however fortunately the lzma extension was useful to identify
that this possibly be uncompressed with 7zip ([lmgtfy lzma file][]). On
ubuntu there is a package called p7zip thus:

~~~~ {lang="bash"}
bryce@sarek:f200$ mv f200_02b7b50f575759cff7.tar.lzma f200_02b7b50f575759cff7.tar.7z
bryce@sarek:f200$ p7zip -d f200_02b7b50f575759cff7.tar.7z

7-Zip (A) 9.04 beta  Copyright (c) 1999-2009 Igor Pavlov  2009-05-30
p7zip Version 9.04 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,8 CPUs)

Processing archive: f200_02b7b50f575759cff7.tar.7z

Extracting  f200_02b7b50f575759cff7.tar

Everything is Ok

Size:       1730560
Compressed: 487746
bryce@sarek:f200$ tar -xf f200_02b7b50f575759cff7.tar
~~~~

This extracts 1121 png image files.

~~~~ {lang="bash"}
bryce@sarek:f200$ ls | head
f200_02b7b50f575759cff7.tar
IMG_0001.png
IMG_0002.png
IMG_0003.png
IMG_0004.png
IMG_0005.png
IMG_0006.png
IMG_0007.png
IMG_0008.png
IMG_0009.png
~~~~

Using *pnginfo* one can verify that each image is similar with respect
to its attributes (width, height, bitdepth, channels, etc.). Using
manual image inspection we see a mostly transparent image with some
white and black pixels. Thus using [python's imaging library][] (PIL) we
simply write a quick program that will combine all the images into one:

~~~~ {lang="python" line="1"}
#!/usr/bin/env python
import Image

def main():
    new = Image.open('IMG_0001.png')
    w, h = new.size
    for i in range(2, 1122):
        im = Image.open('IMG_%04d.png' % i)
        data = im.split()
        for pixel, value in enumerate(im.getdata()):
            if value[3] != 0: # not transparent
                x, y = (pixel % w, pixel * 1. / w)
                new.putpixel((x, y), value)
    new.save('f200_result.png')
    new.show()

if __name__ == '__main__':
    main()
~~~~

Running this eventually produces the following image, from which the
is.gd url [http://is.gd/ced7F][] is the key. Yeah Sexy CPR.

[![Defcon 18 Forensics 200 Result][]][]

  [vnSecurity site]: http://www.vnsecurity.net/2010/05/defcon-18-quals-writeups-collection/
  [f200\_02b7b50f575759cff7.tar.lzma]: http://cs.ucsb.edu/~bboe/public/bin/f200_02b7b50f575759cff7.tar
  [lmgtfy lzma file]: http://lmgtfy.com/?q=lzma+file&l=1
  [python's imaging library]: http://www.pythonware.com/products/pil/
  [http://is.gd/ced7F]: http://is.gd/ced7F
  [Defcon 18 Forensics 200 Result]: /images/2010/05/f200_result-43x300.png
    "Defcon 18 Forensics 200 Result"
  [![Defcon 18 Forensics 200 Result][]]: /images/2010/05/f200_result.png
