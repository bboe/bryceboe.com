#!/usr/bin/env python

import sys

try:
    from MidiOutFile import MidiOutFile
except:
    print 'python midi from http://www.mxm.dk/products/public/pythonmidi'
    sys.exit(1)

CONST = 200

MESG = 'does this not sound super cool?'

def do_stuff(midi):
    notes = [ord(x) for x in MESG]
    prev = None
    midi.update_time(0)
    for note in notes:
        midi.note_on(channel=0, note=note)
        if prev != None:
            midi.update_time(0)
            midi.note_off(channel=0, note=prev)
        prev = note
        midi.update_time(CONST)
    midi.note_off(channel=0, note=prev)

if __name__ == '__main__':
    midi = MidiOutFile('0xDEAFBABE')
    midi.header()
    midi.start_of_track() 
    do_stuff(midi)
    midi.update_time(0)
    midi.end_of_track()
    midi.eof()
