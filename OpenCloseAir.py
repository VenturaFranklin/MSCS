#Created by Elijah Keeswood on 03/12/2022
#MSCS GUI
#Senior Design Team: 22010
#Open Air code

try: #tries to import 
    import RPi.GPIO as io
    import automationhat
    import time
except: #except when it doesn't give you any erros
    pass

def init (DEBUG):
    if not DEBUG:
        if automationhat.is_automation_hat():
            automationhat.light.power.write(1)

#functions for opening and closing valves
def open_air():
    automationhat.relay.one.on()
    
def close_air():
    automationhat.relay.one.off()

def open_gripper():
    print("opening gripper")
    automationhat.relay.two.on()
    automationhat.relay.three.off()


def close_gripper():
    print("closing gripper")
    automationhat.relay.two.off()
    automationhat.relay.three.on()

def turnoffAll_valves():
    print("turning off all valves")
    automationhat.relay.one.off()
    automationhat.relay.two.off()
    automationhat.relay.three.off()
    
    