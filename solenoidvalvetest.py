#!/usr/bin/env python3

import time

import automationhat

def open_valve():
    automationhat.relay.one.on()
    
def close_valve():
    automationhat.relay.one.off()



if automationhat.is_automation_hat():
    automationhat.light.power.write(1)
    
    open_valve()
    time.sleep(1)
    close_valve()

