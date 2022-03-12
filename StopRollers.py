#Created by Elijah Keeswood on 03/12/2022
#MSCS GUI
#Senior Design Team: 22010
#Rollers Off Code
#We don't need this code. Only two lines of code.

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


rollerA_pwm.stop() #ONLY PART WE NEED
rollerB_pwm.stop() 


io.output(roller_standby, False)