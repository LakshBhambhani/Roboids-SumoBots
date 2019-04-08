import PiMotor
from PiMotor import Sensor
import time

m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

motorAll = PiMotor.LinkedMotors(m1, m2, m3, m4)

try:
    motorAll.forward
    time.sleep(0.1)
    motorAll.stop()

except KeyboardInterrupt:
    GPIO.cleanup()
