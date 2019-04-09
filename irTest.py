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
ir3=Sensor("IR3",10)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)

def trigIR():
    ir1.trigger()
    ir2.trigger()
    if ir1.Triggered:
        motorAll.reverse(100)
        time.sleep(0.7)
        motorAll.stop()
        print("Front Line Detected")
    if ir2.Triggered:
        motorAll.forward(100)
        time.sleep(0.7)
        motorAll.stop()
        print("Back Line Detected")

try:
    while true:
        ir3.trigger()
        if ir3.Triggered:
            motorAll.forward(100)
            time.sleep(1)
            motorAll.stop()
    

except KeyboardInterrupt:
    GPIO.cleanup()