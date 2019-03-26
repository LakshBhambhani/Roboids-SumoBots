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

x=0

def trigIR():
    ir1.trigger()
    ir2.trigger()
    if ir1.Triggered:
        motorAll.reverse(70)
        time.sleep(1)
        motorAll.stop()
        print("Front Line Detected")
    if ir2.Triggered:
        motorAll.forward(70)
        time.sleep(1)
        motorAll.stop()
        print("Back Line Detected")

try:
    motorAll.reverse(100)
    trigIR()
    time.sleep(1.7)
    trigIR()
    motorAll.stop()
    trigIR()
    while True:
        us.trigger()
        trigIR()
        if us.Triggered:
            for x in range(10):
                us.trigger()
                trigIR()
                if us.Triggered:
                    motorAll.forward(70)
                    trigIR()
            motorAll.reverse(60)
            trigIR()
            time.sleep(1)
            motorAll.stop()
            trigIR()
        else:
            m1.forward(40)
            trigIR()
            m2.reverse(40)
            trigIR()
            us.trigger()
            trigIR()
            if us.Triggered:
                for x in range(10):
                    us.trigger()
                    trigIR()
                    if us.Triggered:
                        motorAll.forward(100)
                        trigIR()
            time.sleep(0.3)
            motorAll.stop()
            trigIR()
            x=x+1
            print(x)
            if x%3==0:
                trigIR()
                motorAll.forward(40)
                time.sleep(1)
                trigIR()
                motorAll.stop()
                print("x is being 0d")
            trigIR()
        

except KeyboardInterrupt:
    GPIO.cleanup()
            




