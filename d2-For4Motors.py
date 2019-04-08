
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

x=0

def trigIR():
    ir1.trigger()
    ir2.trigger()
    if ir1.Triggered:
        m1.reverse(75)
        m2.reverse(100)
        m3.reverse(100)
        m4.reverse(75)
        time.sleep(0.7)
        motorAll.stop()
        print("Front Line Detected")
    if ir2.Triggered:
        m1.forward(75)
        m2.forward(100)
        m3.forward(100)
        m4.forward(75)
        time.sleep(0.7)
        motorAll.stop()
        print("Back Line Detected")

def forward():
    print("Going forwards...")
    m1.forward(75)
    m2.forward(100)
    m3.forward(100)
    m4.forward(75)
    trigIR()

def reverse():
    print("Going backwards...")
    m1.reverse(75)
    m2.reverse(100)
    m3.reverse(100)
    m4.reverse(75)
    trigIR()

def left():
    print ("Going to the right...")
    m1.reverse(100)
    m2.forward(100)
    m3.forward(100)
    m4.reverse(100)
    time.sleep(0.46)
    motorAll.stop()
    trigIR()

def right():
    print ("Going to the left...")
    m1.forward(100)
    m2.reverse(100)
    m3.reverse(100)
    m4.forward(100)
    time.sleep(0.46)
    motorAll.stop() 
    trigIR()

try:
    print ("Going to the left...")
    m1.reverse(75)
    m2.reverse(90)
    m3.reverse(90)
    m4.forward(75)
    time.sleep(1.2)
    motorAll.stop()
    while True:
        m1.forward(35)
        m4.forward(35)
        trigIR()
        m2.reverse(35)
        m3.reverse(35)
        trigIR()
        us.trigger()
        trigIR()
        time.sleep(0.2)
        trigIR()
        motorAll.stop()
        #Sonic Check
        trigIR() 
        x=x+1 
        if us.Triggered:
            for x in range(10):
                us.trigger()
                trigIR()
                if us.Triggered:
                    forward()
                    trigIR()
            reverse()
            time.sleep(1)
            motorAll.stop()
        if x==17:
            forward()
            trigIR()
            time.sleep(1)
            motorAll.stop()
            x=0
         

except KeyboardInterrupt:
    GPIO.cleanup()
