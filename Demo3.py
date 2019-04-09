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
irFront=Sensor("IR2",1)
irBack=Sensor("IR1",1)
irLeft=Sensor("IR3",1)
irRight=Sensor("IR4",1)

us=Sensor("ULTRASONIC",45)
ir1=Sensor("IR2",10)
ir2=Sensor("IR1",10)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)
rightMotors = PiMotor.LinkedMotors(m1,m2)
leftMotors = PiMotor.LinkedMotors(m3,m4)

def trigIR():
    irFront.trigger()
    irBack.trigger()
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
    if irLeft.Triggered:
        motorAll.reverse(80)
        time.sleep(0.2)
        motorAll.stop()
        leftMotors.forward(80)
        rightMotors.reverse(80)
        time.sleep(0.5)
        motorAll.stop()
    if irRight.Triggered:
        motorAll.reverse(80)
        time.sleep(0.2)
        motorAll.stop()
        leftMotors.reverse(80)
        rightMotors.forward(80)
        time.sleep(0.5)
        motorAll.stop()
        

def findOpponent():
    print("LA: Finding")
    print("Finding")
    trigIR()
    ar.on()
    al.on()
    ab.on()
    af.on()
    loopright = True
    count = 1
    while True:
        trigIR()
        count = count +1
        if count > 1500:
            print ("LA: Not found reversing side")
            loopright = not loopright
            count = 0
        us.boundary = 120
        motorAll.stop()
        us.trigger()
        time.sleep(0.001)
        if us.Triggered:
            print("LA: Found")
            break
            trigIR()
        if loopright:
            leftMotors.forward(80)
            rightMotors.reverse(80)
            trigIR()
        else:
            leftMotors.reverse(80)
            rightMotors.forward(80)
            trigIR()
        time.sleep(0.001)

    if us.Triggered:
        print("LA: Found opponent")
        while us.Triggered:
            us.trigger()
            trigIR()
        if irFront.Triggered or irBack.Triggered:
			print("LA: Not moving forward")
        else:
            motorAll.forward(80)
            print("Found opponent")
            while us.Triggered:
                us.trigger()
                trigIR()
                motorAll.forward(80)
                trigIR()

try:
    al.on()
    ar.on()
    ab.on()
    af.on()
    print ("LA: Going to the center...")
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
