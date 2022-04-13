#Created by Elijah Keeswood on 03/12/2022
#MSCS GUI
#Senior Design Team: 22010
#Water Pump code

try:
    import RPi.GPIO as io
    import time
except:
    pass

io.setwarnings(False)
io.setmode(io.BCM)

#pin assignments
pumpboard_standby = 9
waterpump_pwm_num = 27

waterpump1 = 23
waterpump2 = 18


#pin setups
io.setwarnings(False)

io.setup(waterpump1, io.OUT)
io.setup(waterpump2, io.OUT)

io.setup(pumpboard_standby, io.OUT)

io.setup(waterpump_pwm_num, io.OUT)

waterpump_pwm = io.PWM(waterpump_pwm_num, 1000)
# 
# def init (DEBUG):
#     if not DEBUG:
#         io.setwarnings(False)
#         io.setmode(io.BCM)
# 
#         #pin assignments
#         pumpboard_standby = 9
#         waterpump_pwm_num = 27
# 
#         waterpump1 = 23
#         waterpump2 = 18
# 
# 
#         #pin setups
#         io.setwarnings(False)
# 
#         io.setup(waterpump1, io.OUT)
#         io.setup(waterpump2, io.OUT)
# 
#         io.setup(pumpboard_standby, io.OUT)
# 
#         io.setup(waterpump_pwm_num, io.OUT)
# 
#         waterpump_pwm = io.PWM(waterpump_pwm_num, 1000)


#functions
def startWater():
    waterpump_pwm.start(80)
    io.output(pumpboard_standby, True)
    io.output(waterpump1, True)    
    io.output(waterpump2, False)
    #io.output(pumpboard_standby, False)


def stopWater():
    #stop pwm
    waterpump_pwm.stop()
    io.output(pumpboard_standby, False)

def rinse():
    startWater()
    time.sleep(5)
    stopWater()



