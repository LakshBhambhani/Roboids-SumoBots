import PiMotor
from PiMotor import Sensor
import time

m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

#Names for Individual Arrows
ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3) 
ar = PiMotor.Arrow(4)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)
rightMotors = PiMotor.LinkedMotors(m1,m2)
leftMotors = PiMotor.LinkedMotors(m3,m4)        

try:
    al.on()
    ar.on()
    ab.on()
    af.on()
    m1.forward(100)
    m2.forward(100)
    m3.forward(80)
    m4.forward(80)
    time.sleep(100)

except KeyboardInterrupt:
    motorAll.stop() 
    GPIO.cleanup()
