#!/usr/bin/env python
import os, sys, Image

if __name__ == '__main__':
    def usage(msg=None):
        if msg:
            sys.stderr.write('%s\n' % msg)
        sys.stderr.write('Usage: %s base modified\n' %
                         os.path.basename(sys.argv[0]))
        sys.exit(1)

    if len(sys.argv) != 3:
        usage()
    elif not os.path.isfile(sys.argv[1]):
        usage('%s is not a file' % sys.argv[1])
    elif not os.path.isfile(sys.argv[2]):
        usage('%s is not a file' % sys.argv[2])

    base_file = sys.argv[1]
    modified_file = sys.argv[2]

    base = Image.open(base_file)
    modified = Image.open(modified_file)
    
    base_flat = tuple(base.getdata())
    modified_flat = tuple(modified.getdata())

    d = []
    for i, bp in enumerate(base_flat):
        mp = modified_flat[i]
        if bp != mp:
            d.append(mp-bp)

    print ''.join([chr(sum(x)) for x in zip(d[::3], d[1::3], d[2::3])])
