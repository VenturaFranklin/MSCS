#Created by Elijah Keeswood on 03/12/2022
#MSCS GUI
#Senior Design Team: 22010
#Open Air code

import RPi.GPIO as io
import automationhat
import time

def open_main():
    automationhat.relay.one.on()
    
def close_main():
    automationhat.relay.one.off()

def open_gripper():
    automationhat.relay.two.on()
    
def close_gripper():
    automationhat.relay.two.off()

def open_dry():
    automationhat.relay.three.on()
    
def close_dry():
    automationhat.relay.three.off()


if automationhat.is_automation_hat():
    automationhat.light.power.write(1)
    