#Created by Elijah Keeswood on 3/9/2022
#MSCS GUI
#Senior Design Team: 22010
#Start Rollers

import RPi.GPIO as io
import time

io.setmode(io.BCM)

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

#pin setups
io.setwarnings(False)

io.setup(rollerA1, io.OUT)
io.setup(rollerA2, io.OUT)

io.setup(roller_standby, io.OUT)

io.setup(rollerA_pwm, io.OUT)
rollerA_pwm = io.PWM(rollerA_pwm, 1000)

io.setup(rollerB_pwm, io.OUT)
rollerB_pwm = io.PWM(rollerB_pwm, 1000)

io.output(roller_standby, True)


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
    #start pwm
    rollerA_pwm.start(100)
    rollerB_pwm.start(100)

    #Main Process
    inwards()
    
def stopRollers():
    rollerA_pwm.stop()
    rollerB_pwm.stop()


io.output(roller_standby, False)
