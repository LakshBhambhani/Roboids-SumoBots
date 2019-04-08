import PiMotor
from PiMotor import Sensor
import time


m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

us=Sensor("ULTRASONIC",30)
ir1=Sensor("IR1",10)
ir2=Sensor("IR2",10)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)

def TrigIR():
    ir1.trigger()
    ir2.trigger()
    if ir1.Triggered:
        print("Front Line Detected")
    if ir2.Triggered:
        print("Back Line Detected")

while True:
    TrigIR()