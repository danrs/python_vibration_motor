# To ust this example, connect your sensor to AIN0.
# If using a grove module and beaglebone grove cape,
# use the J3 grove socket on the cape.

import time
import python_vibration_motor as v_motor

motor1 = v_motor.vibration_motor()
while True:
    motor1.toggle()
    if(motor1.status() = 0):
        print "Motor off"
    else:
        print "Motor on"
    time.sleep(0.5)
