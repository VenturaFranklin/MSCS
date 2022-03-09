#Created by Elijah Keeswood on 3/9/2022

#MSCS 
#Start Rollers

import RPi.GPIO as io
import time

io.setmode(io.BCM)

#roller board standby pins
roller_standby = 10
#rollers A and B pwm pins
rollerA_pwm = 4
rollerB_pwm = 17
#rollers A and B input output pins
rollerA1 = 11
rollerA2 = 0
rollerB1 = 14
rollerB2 = 15

io.setwarnings(False)
io.setup(rollerA1, io.OUT)
io.setup(rollerA2, io.OUT)
io.setup(roller_standby, io.OUT)
io.setup(rollerA_pwm, io.OUT)
rollerA_pwm = io.PWM(rollerA_pwm, 1000)

io.output(roller_standby, True)

def clockwise():
    io.output(rollerA1, True)    
    io.output(rollerA2, False)

def counter_clockwise():
    io.output(rollerA1, False)
    io.output(rollerA2, True)


rollerA_pwm.start(100)

counter_clockwise()
sleep(2)
rollerA_pwm.stop()


io.output(standby_pin, False)
