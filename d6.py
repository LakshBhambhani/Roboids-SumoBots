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
irLeft=Sensor("IR3",1)
irRight=Sensor("IR4",1)

motorSpeed = 10

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)
rightMotors = PiMotor.LinkedMotors(m1,m2)
leftMotors = PiMotor.LinkedMotors(m3,m4)

def trigIR():
    irFront.trigger()
    irBack.trigger()
    irLeft.trigger()
    irRight.trigger()
    if irFront.Triggered:
        motorAll.reverse(100)
        time.sleep(1.2)
        motorAll.stop()
        print("LA: Front Line Detected")
    if irBack.Triggered:
        motorAll.forward(100)
        time.sleep(1.2)
        motorAll.stop()
        print("LA: Back Line Detected")

def findOpponent():
    print("LA: Finding")
    print("Finding")
    trigIR()
    motorSpeed = 40
    while True:
	print("LA: ")
	print(us.lastRead)
        trigIR()
        us.boundary = 80
        us.trigger()
        time.sleep(0.001)
        motorAll.stop()
        if us.Triggered:
            print("LA: Found")
            trigIR()
            break
            
        leftMotors.forward(45)
        rightMotors.reverse(45)
        trigIR()
        time.sleep(0.000001)

    if us.Triggered:
        print("LA: Found opponent")
        count = 0
	trigIR()
	while us.Triggered and count < 2:
	    trigIR()
	    print("LA: ")
	    print(us.lastRead)
	    print("Motorspeed: ")
	    print(motorSpeed)
	    print("Count:")
	    print(count)
	    us.trigger()
	    trigIR()
	    if irFront.Triggered:
	    	count = count + 1
		if count == 2:
			leftMotors.forward(100)
			rightMotors.reverse(100)
			trigIR()
			time.sleep(0.5)
            if us.lastRead <= 7 and not irFront.Triggered and not irBack.Triggered:
                motorSpeed = 100
            else:
                motorSpeed = 30
            motorAll.forward(motorSpeed)
        

try:
    al.on()
    ar.on()
    ab.on()
    af.on()
    print ("LA: Going to the center...")
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
    GPIO.cleanup()
