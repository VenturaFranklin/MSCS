import RPi.GPIO as io
from time import sleep

io.setmode(io.BCM)

standby_pin = 27

a_pwm_pin = 18
a1_pin = 4
a2_pin = 17

io.setwarnings(False)
io.setup(a1_pin, io.OUT)
io.setup(a2_pin, io.OUT)
io.setup(standby_pin, io.OUT)
io.setup(a_pwm_pin, io.OUT)
a_pwm = io.PWM(a_pwm_pin, 1000)

io.output(standby_pin, True)

def clockwise():
    io.output(a1_pin, True)    
    io.output(a2_pin, False)

def counter_clockwise():
    io.output(a1_pin, False)
    io.output(a2_pin, True)

a_pwm.start(100)

counter_clockwise()
sleep(2)

a_pwm.stop()
io.output(standby_pin, False)