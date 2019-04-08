import PiMotor
from PiMotor import Sensor
import time


m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

us=Sensor("ULTRASONIC",60)
ir1=Sensor("IR2",10)
ir2=Sensor("IR1",10)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)

try:
    m1.forward(100)
    time.sleep(3)
    m1.stop()
    m2.forward(100)
    time.sleep(3)
    m2.stop()
    m3.forward(100)
    time.sleep(3)
    m3.stop()
    m4.forward(100)
    time.sleep(3)
    m4.stop()

except KeyboardInterrupt:
    GPIO.cleanup()