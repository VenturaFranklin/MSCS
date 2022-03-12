#Created by Elijah Keeswood on 03/12/2022
#MSCS GUI
#Senior Design Team: 22010
#Start Water Pump code

import RPi.GPIO as io
import time

io.setmode(io.BCM)

#pin assignments
pumpboard_standby = 9
waterpump_pwm = 22

waterpump1 = 24
waterpump2 = 25

#pin setups
io.setwarnings(False)

io.setup(waterpump1), io.OUT)
io.setup(waterpump2, io.OUT)

io.setup(pumpboard_standby, io.OUT)

io.setup(waterpump_pwm, io.OUT)

waterpump_pwm = io.PWM(waterpump_pwm, 1000)

io.output(pumpboard_standby, True)

#functions
def dispenseWater():
    io.output(waterpump1, True)    
    io.output(waterpump2, False)

    time.sleep(10) #time can change
    
    #stop pwm
    waterpump_pwm.stop()

io.output(pumpboard_standby, False)

