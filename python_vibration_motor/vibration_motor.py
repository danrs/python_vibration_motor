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
    def __init__(self, pin="P9_17", status=GPIO.LOW):
        """
        The Adafruit_BBIO library will accept pins as numbers (eg. "P9_17")
        or pin names (eg "GPIO_5"). There are many GPIO pins, but some are
        used for other features (eg UART) if that feature is enabled. Note
        that sometimes the GPIO name doesn't work correctly (eg for GPIO_5)
        so using PX_XX names instead is recommended
        
        """
        pin_number_re = re.compile('P[89]_([1-9]?[0-9])', re.IGNORECASE)
        pin_name_re = re.compile('GPIO_([1-9]?[0-9]?[0-9])', re.IGNORECASE)
        if not re.match(pin_name_re,pin):
            match = re.match(pin_number_re,pin)
            if match is None:
                raise ValueError('pin must be valid gpio pin like P9_17 or GPIO_5')
        self.pin = pin
        self.status = status
        GPIO.setup(self.pin, GPIO.OUT);
        GPIO.output(self.pin, self.status);

    def getStatus(self):
        """
        Return current motor status (on/off)
        """
        return self.status
    def on(self):
        """
        Turn motor on
        """
        GPIO.output(self.pin, GPIO.HIGH)
        self.status = GPIO.HIGH
    def off(self):
        """
        Turn motor off
        """
        GPIO.output(self.pin, GPIO.LOW)
        self.status = GPIO.LOW
    def toggle(self):
        """
        Toggle motor status (on/off
        """
        if(self.status == GPIO.HIGH):
            self.off()
        else:
            self.on()
