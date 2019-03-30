import PiMotor
from PiMotor import Sensor
import time


m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

us=Sensor("ULTRASONIC",30)
ir1=Sensor("IR1",4)
ir2=Sensor("IR2",4)

#M1 = BL
#M2 = BR
#M3 = FR
#M4 = FL


#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)

try:
    m1.forward(75)
    m2.forward(100)
    m3.forward(100)
    m4.forward(75)
    time.sleep(3)
    motorAll.stop()

except KeyboardInterrupt:
    GPIO.cleanup()
