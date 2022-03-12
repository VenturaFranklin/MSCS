#Created by Elijah Keeswood on 03/12/2022
#MSCS GUI
#Senior Design Team: 22010
#Dispense Reagents code

import RPi.GPIO as io
import time

io.setmode(io.BCM)

#pin assignments
pumpboard_standby = 9
peristaltic_pwm = 27
waterpump_pwm = 22

peristaltic1 = 18
peristaltic2 = 23

waterpump1 = 24
waterpump2 = 25

#pin setups
io.setwarnings(False)

io.setup(peristaltic1), io.OUT)
io.setup(peristaltic2, io.OUT)

io.setup(waterpump1), io.OUT)
io.setup(waterpump2, io.OUT)

io.setup(pumpboard_standby, io.OUT)

io.setup(peristaltic_pwm, io.OUT)
io.setup(waterpump_pwm, io.OUT)

peristaltic_pwm = io.PWM(peristaltic_pwm, 1000)
waterpump_pwm = io.PWM(waterpump_pwm, 1000)

io.output(pumpboard_standby, True)

#functions
def dispenseWater():
    io.output(waterpump1, True)    
    io.output(waterpump2, False)

def dispenseSoap():
    io.output(peristaltic1, True)
    io.output(peristaltic2, False)

def dispenseReagents(): #main
    #start pwm
    peristaltic_pwm.start(100)
    waterpump_pwm.start(100)

    #Main Process
    dispenseSoap()
    dispenseWater()
    time.sleep(2)

    #stop pwm
    peristaltic_pwm.stop()
    waterpump_pwm.stop()

io.output(pumpboard_standby, False)

