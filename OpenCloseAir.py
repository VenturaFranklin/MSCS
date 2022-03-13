#Created by Elijah Keeswood on 03/12/2022
#MSCS GUI
#Senior Design Team: 22010
#Open Air code

import RPi.GPIO as io
import automationhat
import time


if automationhat.is_automation_hat():
    automationhat.light.power.write(1)

#functions for opening and closing valves
def open_air():
    automationhat.relay.one.on()
    
def close_air():
    automationhat.relay.one.off()

def open_gripper():
    automationhat.relay.two.on()
    automationhat.relay.three.off()

def close_gripper():
    automationhat.relay.two.off()
    automationhat.relay.three.on()

    