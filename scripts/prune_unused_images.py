#!/usr/bin/env python
import os
import sys

def main():
    files = set()
    for dirpath, dirnames, filenames in os.walk('content/images'):
        if not dirnames and not filenames:
            os.rmdir(dirpath)
        if filenames:
            files |= set([os.path.join(dirpath, x) for x in filenames])
    for filename in files:
        print filename[8:]

if __name__ == '__main__':
    sys.exit(main())
