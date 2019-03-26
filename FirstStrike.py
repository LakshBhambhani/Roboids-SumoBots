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


direction = input("Right or Left?")
print (direction)


            
def TrigIR():
    ir1.trigger()
    ir2.trigger()
    if ir1.Triggered or ir2.Triggered:
        motorAll.reverse(100)
        time.sleep(2)
        motorAll.stop()

if (direction == "right"):
    print ("Going to the right...")
    m1.forward(100)
    m2.forward(80)
    TrigIR()


if (direction == "left"):
    print ("Going to the left...")
    m1.forward(80)
    m2.forward(100)
    TrigIR()
    
except KeyboardInterrupt:
GPIO.cleanup()
