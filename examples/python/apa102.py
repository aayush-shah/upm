#!/usr/bin/python
# Author:  Yannick Adam <yannick.adam@gmail.com>
# Copyright (c) 2016 Yannick Adam
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import time, sys, signal, atexit
import pyupm_apa102 as mylib

def main():
    # Instantiate a strip of 30 LEDs on SPI bus 0
    ledStrip = mylib.APA102(30, 0, False)

    ## Exit handlers ##
    # This stops python from printing a stacktrace when you hit control-C
    def SIGINTHandler(signum, frame):
        raise SystemExit

    # Register exit handlers
    signal.signal(signal.SIGINT, SIGINTHandler)

    print "Setting all LEDs to Green"
    ledStrip.setAllLeds(31, 0, 255, 0)

    print "Setting LEDs between 10 and 20 to Red"
    ledStrip.setLeds(10, 20, 31, 255, 0, 0)

    print "Setting LED 15 to Blue"
    ledStrip.setLed(15, 31, 0, 0, 255)

if __name__ == '__main__':
    main()
