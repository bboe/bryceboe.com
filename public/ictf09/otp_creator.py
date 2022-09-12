#!/usr/bin/env python
import os, random, sys

if __name__ == '__main__':
    off = 95
    pass_phrase = 'nudibranchescanbefoundaroundthechannelislands'[::-1]

    phrase = sys.stdin.read()
    phrase_vals = [ord(x) - off for x in phrase]

    while True:
        print 'looping'
        positions = []
        remaining = len(pass_phrase)
        otp_vals = [random.randint(0, 25) for x in phrase]
        otp = ''.join([chr(x + off) for x in otp_vals])
        modified_otp = ''
        for i, char in enumerate(otp):
            if remaining == 0 or char != pass_phrase[-remaining]:
                modified_otp += char
            else:
                positions.append(i)
                remaining -= 1
        if remaining == 0: break
            

    encrypted = ''.join([chr(x + off) for x in map(lambda x,y:x^y,
                                                   phrase_vals, otp_vals)])


    print "===ONE TIME PAD==="
    print otp
    print "=NEW 1 TIME PAD==="
    print modified_otp
    print "====ENCRYPTED====="
    print encrypted
    print '=================='
    print positions
