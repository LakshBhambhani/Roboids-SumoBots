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
irFront=Sensor("IR1",1)
irBack=Sensor("IR2",1)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)
rightMotors = PiMotor.LinkedMotors(m1,m2)
leftMotors = PiMotor.LinkedMotors(m3,m4)

def trigIR():
    irFront.trigger()
    irBack.trigger()
    if irFront.Triggered:
        motorAll.reverse(100)
        time.sleep(1)
        motorAll.stop()
        us.boundary = 120
        print("Front Line Detected")
    if irBack.Triggered:
        motorAll.forward(100)
        time.sleep(1)
        motorAll.stop()
        us.boundary = 120
        print("Back Line Detected")

def findOpponent():
    print("Finding")
    trigIR()
    while True:
        trigIR()
        us.boundary = 122
        us.trigger()
        time.sleep(0.001)
        motorAll.stop()
        if us.Triggered:
            print("Found")
            trigIR()
            break
        leftMotors.forward(75)
        rightMotors.reverse(75)
        trigIR()
        time.sleep(0.001)
       

    if us.Triggered:
        print("Found opponent")
        count = 0
        while us.Triggered and count <= 2:
	        print("count:")
	        print(count)
                if irFront.Triggered:
	    	        count = count + 1
	        us.trigger()
	        trigIR()
                if us.lastRead <= 3 and not irFront.Triggered:
                    motorSpeed = 100
                else:
                    motorSpeed = 65
                motorAll.forward(motorSpeed)

    if count == 2:
        rightMotors.reverse(100)
        leftMotors.forward(100)
        time.sleep(0.8)
        motorAll.stop()
        count = 0
        

try:
    al.on()
    ar.on()
    ab.on()
    af.on()
    print ("Going to the center...")
    m1.reverse(70)
    m2.reverse(70)
    m3.reverse(100)
    m4.reverse(100)
    time.sleep(1.8)
    motorAll.stop()
    while True:
        findOpponent()

except KeyboardInterrupt:
    motorAll.stop() 