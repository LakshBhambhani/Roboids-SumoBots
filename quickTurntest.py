import PiMotor
from PiMotor import Sensor
import time

m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

us=Sensor("ULTRASONIC",45)
ir1=Sensor("IR2",10)
ir2=Sensor("IR1",10)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)
leftMotors = PiMotor.LinkedMotors(m1, m2)
rightMotors = PiMotors.LinkedMotors(m3, m4)

try:
    leftMotors.forward(80)
    rightMotors.reverse(80)
    time.sleep(5)
    motorAll.stop()

except KeyboardInterrupt:
    GPIO.cleanup()