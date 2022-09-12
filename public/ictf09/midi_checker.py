#!/usr/bin/env python

import sys

try:
    from MidiOutStream import MidiOutStream
    from MidiInFile import MidiInFile
except:
    print 'python midi from http://www.mxm.dk/products/public/pythonmidi'
    sys.exit(1)


notes = ''

class Notes(MidiOutStream):
    def note_on(self, channel, note, velocity):
        global notes
        notes += chr(note)

if __name__ == '__main__':
    midi = MidiInFile(Notes(), '0xDEAFBABE')
    midi.read()
    print notes
