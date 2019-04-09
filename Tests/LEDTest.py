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

us=Sensor("ULTRASONIC",120)
ir1=Sensor("IR2",10)
ir2=Sensor("IR1",10)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)
leftMotors = PiMotor.LinkedMotors(m1,m2)
rightMotors = PiMotor.LinkedMotors(m3,m4)

try:
    al.on()
    ar.on()
    ab.on()
    af.on()
    time.sleep(5)
    al.off()
    ar.off()
    ab.off()
    af.off()

except KeyboardInterrupt:
    GPIO.cleanup()
