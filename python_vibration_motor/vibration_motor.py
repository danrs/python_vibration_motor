# Copyright (c) 2016 Daniel Smith
# Author: Daniel Smith
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import re
import Adafruit_BBIO.GPIO as GPIO

class vibration_motor:
    # Default pin
    pin = "GPIO_5"
    status = GPIO.LOW
    def init(self, pin):
        # The Adafruit_BBIO library will accept pins as numbers (eg. "P9_17")
        # or pin names (eg "GPIO_5"). THere are many GPIO pins, but some are
        # used for other features (eg UART) if that feature is enabled.
        #
        pin_number_re = re.compile('P[89]_([1-9]?[0-9])')
        pin_name_re = re.compile('GPIO_([1-9]?[0-9]?[0-9])')
        if not re.match(pin_name_re,pin,re.IGNORECASE):
            match = re.match(pin_number_re,pin,re.IGNORECASE)
            if match is None:
                raise ValueError('pin must be valid gpio pin like P9_17 or GPIO_5')
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT);
        GPIO.output(self.pin, GPIO.LOW);

    def getStatus(self):
        return self.status
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
    def toggle(self):
        GPIO.output(self.pin, (1+self.status)%2) # invert current status 1<->0
