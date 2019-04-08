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
leftMotors = PiMotor.LinkedMotors(m1,m2)
rightMotors = PiMotor.LinkedMotors(m3,m4)

try:
    for x in range(100):
        us.trigger()
        time.sleep(0.001)
    
except KeyboardInterrupt:
    GPIO.cleanup()