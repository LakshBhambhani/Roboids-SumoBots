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
#M1 = BL #M2 = BR #M3 = FR #M4 = FL 
# #To drive all motors together 
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4) 
try: 
    #To turn around: # m1.forward(100) 
    # m2.reverse(100) 
    # m3.reverse(100)
    # m4.forward(100)
    # time.sleep(0.9) 
    # motorAll.stop() 
    
    #To do a 90 degree turn right: 
    # m1.forward(100) 
    # m2.reverse(100) 
    # m3.reverse(100) 
    # m4.forward(100) 
    # time.sleep(0.46)
    # motorAll.stop() 
    
    #To do a 90 degree turn left: 
    #m1.reverse(100) 
    #m2.forward(100) 
    #m3.forward(100) 
    #m4.reverse(100) 
    #time.sleep(0.46) 
    #motorAll.stop() 

except KeyboardInterrupt: 
    GPIO.cleanup()