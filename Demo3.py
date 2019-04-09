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

def trigIR():
    ir1.trigger()
    ir2.trigger()
    ir1.boundary = 10
    ir2.boundary = 10
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

def findOpponent():
    print("Finding")
    loopright = True
    count = 1
    while True:
        trigIR()
        count = count +1
        if count > 1500:
            print ("Not found reversing side")
            loopright = not loopright
            count = 0
        motorAll.stop()
        us.boundary = 120
        us.trigger()
        time.sleep(0.001)
        if us.Triggered:
            print("Found")
            break
        if loopright:
            leftMotors.forward(80)
            rightMotors.reverse(80)
        else:
            leftMotors.reverse(80)
            rightMotors.forward(80)
        time.sleep(0.001)

    if us.Triggered:
            print("Found opponent")
            while us.Triggered:
                us.trigger()
                trigIR()
                motorAll.forward(80)

try:
    al.on()
    ar.on()
    ab.on()
    af.on()
    print ("Going to the left...")
    m1.reverse(35)
    m2.reverse(35)
    m3.reverse(50)
    m4.reverse(50)
    time.sleep(1.2)
    motorAll.stop()
    while True:
        findOpponent()

except KeyboardInterrupt:
    motorAll.stop() 
    GPIO.cleanup()