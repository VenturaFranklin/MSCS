#Created by Elijah Keeswood on 03/12/2022
#MSCS GUI
#Senior Design Team: 22010
#Dispense Reagents Code
try:
    import RPi.GPIO as io
    import time
except: pass

#pin assignments
pumpboard_standby = 9
peristaltic_pwm_num = 22

peristaltic1 = 24
peristaltic2 = 25


#pin setups
io.setwarnings(False)

io.setup(peristaltic1, io.OUT)
io.setup(peristaltic2, io.OUT)


io.setup(pumpboard_standby, io.OUT)
io.setup(peristaltic_pwm_num, io.OUT)

peristaltic_pwm = io.PWM(peristaltic_pwm_num, 1000)
# 
# def init (DEBUG):
#     if not DEBUG:
#         io.setmode(io.BCM)
# 
#         #pin assignments
#         pumpboard_standby = 9
#         peristaltic_pwm_num = 22
# 
#         peristaltic1 = 24
#         peristaltic2 = 25
# 
# 
#         #pin setups
#         io.setwarnings(False)
# 
#         io.setup(peristaltic1, io.OUT)
#         io.setup(peristaltic2, io.OUT)
# 
# 
#         io.setup(pumpboard_standby, io.OUT)
#         io.setup(peristaltic_pwm_num, io.OUT)
# 
#         peristaltic_pwm = io.PWM(peristaltic_pwm_num, 1000)



#functions
def startSoap():
    peristaltic_pwm.start(100)
    io.output(pumpboard_standby, True)
    io.output(peristaltic1, True)
    io.output(peristaltic2, False)

def stopSoap():
    #stop pwm
    peristaltic_pwm.stop()
    io.output(pumpboard_standby, False)
    



