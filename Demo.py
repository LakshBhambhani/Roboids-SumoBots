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

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)

try:
    while True:
        motorAll.reverse(60)
        time.sleep(0.3)
        TrigIR()
        m1.reverse(100)
        time.sleep(0.1)
        motorAll.reverse(100)
        TrigIR()
        time.sleep(1)
        motorAll.stop()
        TrigIR()
        while True:
            TrigIR()
            us.trigger()
            if us.Triggered:
                while us.Triggered:
                    motorAll.forward(100)
                    TrigIR()
                motorAll.reverse(100)
                TrigIR()
                time.sleep(1)
                motorAll.stop()
            else:
                motorAll.forward(100)
                TrigIR()
                time.sleep(1)
                motorAll.stop()
                TrigIR()
                m2.forward(100)
                TrigIR()
                us.trigger()
                time.sleep(0.5)
                TrigIR()
                motorAll.stop()
            
def TrigIR():
    ir1.trigger()
    ir2.trigger()
    if ir1.Triggered or ir2.Triggered:
        motorAll.reverse(100)
        time.sleep(2)
        motorAll.stop()


except KeyboardInterrupt:
    GPIO.cleanup()
