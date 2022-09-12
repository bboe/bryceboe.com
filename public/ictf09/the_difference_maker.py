#!/usr/bin/env python
import os, sys, Image

if __name__ == '__main__':
    def usage(msg=None):
        if msg:
            sys.stderr.write('%s\n' % msg)
        sys.stderr.write('Usage: %s image message\n' %
                         os.path.basename(sys.argv[0]))
        sys.exit(1)

    if len(sys.argv) != 3:
        usage()
    elif not os.path.isfile(sys.argv[1]):
        usage('%s is not a file' % sys.argv[1])
    original_file = sys.argv[1]
    message = sys.argv[2]
    print 'Hiding Message: %s' % message

    im = Image.open(original_file)
    
    flat = tuple(im.getdata())
    pixels = zip(flat[::3], flat[1::3], flat[2::3])

    remaining = len(message)

    for i, pixel in enumerate(pixels):
        if remaining == 0: break
        if pixel[0] < pixel[1] < pixel[2] and pixel[2] < 75:
            v = ord(message[-remaining])
            a = b = v / 3
            c = v - a - b
            pixels[i] = (pixel[0] + a, pixel[1] + b, pixel[2] + c)
            remaining -= 1

    if remaining > 0:
        sys.stderr.write('Not enough pixels for text\n')
        sys.exit(1)

    flat = []
    [flat.extend(x) for x in pixels]
    im.putdata(flat)

    temp = original_file.split('.')
    im.save('%s-new.%s' % (''.join(temp[:-1]), temp[-1]))
    
    
