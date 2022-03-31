#Created by Elijah Keeswood on 3/9/2022
#MSCS GUI
#Senior Design Team: 22010
#Start Rollers


import time

try: #Try importing these
    import RPi.GPIO as io
    import board
    from adafruit_motorkit import MotorKit

except: #except when it doensn't give you an error
    pass

def init(DEBUG):
    if not DEBUG:    
        io.setmode(io.BCM)
        kit = MotorKit(i2c=board.I2C())
        #roller board standby pins
        roller_standby = 10
        #rollers A and B pwm pins
        rollerA_pwm = 17
        rollerB_pwm = 4
        #rollers A and B input output pins
        rollerA1 = 11
        rollerA2 = 0
        rollerB1 = 14
        rollerB2 = 15

        oldHatFlag = True
        #pin setups
        io.setwarnings(False)

        io.setup(rollerA1, io.OUT)
        io.setup(rollerA2, io.OUT)

        io.setup(roller_standby, io.OUT)

        io.setup(rollerA_pwm, io.OUT)
        rollerA_pwm = io.PWM(rollerA_pwm, 1000)

        io.setup(rollerB_pwm, io.OUT)
        rollerB_pwm = io.PWM(rollerB_pwm, 1000)




#Rolling functions
def inwards():
    io.output(rollerA1, True)    
    io.output(rollerA2, False)

    io.output(rollerB1, False)    
    io.output(rollerB2, True)

def outwards():
    io.output(rollerA1, False)
    io.output(rollerA2, True)

    io.output(rollerB1, True)
    io.output(rollerB2, False)

def startRollers():
    if oldHatFlag:
        kit.motor1.throttle = 1
        kit.motor2.throttle = -1
    else:
        #start pwm
        rollerA_pwm.start(100)
        rollerB_pwm.start(100)
        #Main Process
        inwards()
        io.output(roller_standby, True)
    
def stopRollers():
    if oldHatFlag:
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
    else:
        rollerA_pwm.stop()
        rollerB_pwm.stop()
        io.output(roller_standby, False)



