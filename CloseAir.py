#Created by Elijah Keeswood on 03/12/2022
#MSCS GUI
#Senior Design Team: 22010
#Close Air code

import RPi.GPIO as io
import automationhat
import time

#def open_valve():
 #   automationhat.relay.one.on()
    
def close_valve():
    automationhat.relay.one.off()


if automationhat.is_automation_hat():
    automationhat.light.power.write(1)
    
    #open_valve()
    #time.sleep(1)
    close_valve()