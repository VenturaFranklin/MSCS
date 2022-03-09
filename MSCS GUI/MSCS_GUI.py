#Created by Elijah Keeswood on 03/08/2022
#Copyright @ 2022 Elijah Keeswood. All rights reserved.
#MSCS GUI
#Senior Design Team: 22010

#Import tkinter library
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog #For accessing computers files
##Imports for Raspberry Pi
import time
#import board
#from adafruit_motorkit import MotorKit
#import RPi.GPIO as GPIO
##Imports for Automation Hat
#import automationhat
#import RPi.GPIO as io
#from time import sleep

##Hardware
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(26, GPIO.OUT)
# GPIO.output(26, GPIO.HIGH)
# time.sleep(1)
# GPIO.output(26, GPIO.LOW)



#Variables
LARGE_FONT = ("Verdana", 12)



class MainClass(tk.Tk):                                      #BASELINE of code for creating and opening a page and moving from page to page
                         #Sea of BTC app is just business, can define as anything, changed to Main class
                         #can usually end in : but (tk.Tk) is inheritance 
    def __init__ (self, *args, **kwargs):
                        #def __init is a method acts like a fxn. Initializes stuff. Does thing first on startup liking being able to use a 
                        #mouse when computer boots up.
                        #self(1st parameter eh), args(arguments= can pass any # of variables), kwargs(keyword arguments = passing thru dictionaries) 
                        #are just convention, could look like (butt, *, **) but people can recognize former

        tk.Tk.__init__(self,*args, **kwargs)    #initializes tkinter
        container = tk.Frame (self)             #container and frame(window) apart of tkinter
        container.pack(side="top", fill="both", expand=True) #top of window, fills in space, expand (if theres any white space then we can expand)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}                    #dictionary for all the frames


        #####**********             When adding a new page just add it to this for loop list                    *******####

        for F in (StartPage, ComponentsPage, RollersPage, LinActPage, PumpsPage, SolValPage):      
        #for Frame in startpage and page one, saves frame to self.frames{} dictionary. 
                                                    #So when def show_frame it shows current frame.      
            frame = F(container, self)  #pass through container and self
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")     #grid is 2nd (pack being 1st) layout format "superior"
            #frame.grid(row=110, column=110, sticky="nsew")#110 dimensions don't make it huge, but will order it based on which one is greater/lesser
                                                           #sticky = alignment + stretch
                                                           #nsew = north south east west, stretches in every direction. 
                                                           #if "ns" then it would stretch top to bottom but not side to side

        self.show_frame(StartPage)  #show frame defined below. Shows start page.
    #DONE W/ initializing  

    def show_frame(self, cont): #Shows frame: startpage, pageone, pagetwo, etc.
        frame = self.frames[cont]   #corresponds w/ self.frames{}. cont=container is the key which looks for the frame.
        frame.tkraise()             #raises window to front. When key is found it brings to front.


#functions for stuff
def stopClean():
    print("stopped cleaning")

def mrClean():
    cleanPopup = tk.Tk()
    cleanPopup.title("Cleaning")
    button = tk.Button(cleanPopup, text = "Stop", command = stopClean)
    button.pack()

    print ("Go to Home")
    print("take picture")
    print("Start Rollers")
    print("Dispense Reagent")
    time.sleep(3)
    print("Go to Bottom")

    print("CLEAN OSCILLATE")
    print("Rollers off")
    print("Start Water Pump")
    print("Open Air")
    print("DRYING OSCILLATE")
    cleanPopup.mainloop()

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/") #opens and displays file explorer
      


class StartPage(tk.Frame):                                 #The Start Page. tk.Frame inherits so we don't have to call.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
      #  tk.geometry('300x200')
        label = tk.Label(self, text="MSCS Main Page", font = LARGE_FONT) #class is tk.label() which creates the object = label. 
                                                             #LARGE_FONT defined at the top
        label.pack(pady=10, padx=10) #pad puts padding on it. looks nice.

        button1 = tk.Button(self, text="CLEAN", command = mrClean)
        button1.pack()

        button2 = tk.Button(self, text="Components", 
                            command = lambda: controller.show_frame(ComponentsPage)) 
                                     #lambda creates a quick throwaway fxn. Only here when we call it.
                                     #can also pass variables through; command = lambda: fxn("sus")
                                                                   #ComponentsPage is a class                        
        button2.pack()
        
        button4 = tk.Button(self, text="Files", command = browseFiles) #calls to browse files explorer
        button4.pack()


class ComponentsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Components", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="Rollers",
                            command=lambda: controller.show_frame(RollersPage))
        button2.pack()

        button3= tk.Button(self, text="Linear Actuator",
                            command=lambda: controller.show_frame(LinActPage))
        button3.pack()

        button4 = tk.Button(self, text="Pumps",
                            command=lambda: controller.show_frame(PumpsPage))
        button4.pack()

        button1 = tk.Button(self, text="Back to Home",                          #doesn't matter what button variable is called. its unique to class
                            command = lambda: controller.show_frame(StartPage)) 
        button1.pack()

##Integrated code
#def dcMotors(): #DC Motors test by Richard
#    io.setmode(io.BCM)

#    standby_pin = 27

#    a_pwm_pin = 18
#    a1_pin = 4
#    a2_pin = 17

#    io.setwarnings(False)
#    io.setup(a1_pin, io.OUT)
#    io.setup(a2_pin, io.OUT)
#    io.setup(standby_pin, io.OUT)
#    io.setup(a_pwm_pin, io.OUT)
#    a_pwm = io.PWM(a_pwm_pin, 1000)

#    io.output(standby_pin, True)

#    def clockwise():
#        io.output(a1_pin, True)    
#        io.output(a2_pin, False)

#    def counter_clockwise():
#        io.output(a1_pin, False)
#        io.output(a2_pin, True)

#    a_pwm.start(100)

#    counter_clockwise()
#    sleep(2)

#    a_pwm.stop()
#    io.output(standby_pin, False)

class RollersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Rollers", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        #button3 = tk.Button(self, text="Run DC motors", command = dcMotors)
        #button3.pack()

        button2 = tk.Button(self, text="Components",                       
                            command = lambda: controller.show_frame(ComponentsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home",                         
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

class LinActPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Linear Actuator", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="Components",                       
                            command = lambda: controller.show_frame(ComponentsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home",         
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

class PumpsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Pumps", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button3 = tk.Button(self, text="Solenoid Valves",                        
                            command = lambda: controller.show_frame(SolValPage))
        button3.pack()

        button2 = tk.Button(self, text="Components",                         
                            command = lambda: controller.show_frame(ComponentsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home",                        
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

##Integrated Code
#def SolValves(): #Solenoid Valves Test by Richard
#    def open_valve():
#        automationhat.relay.one.on()
    
#    def close_valve():
#        automationhat.relay.one.off()

#    if automationhat.is_automation_hat():
#        automationhat.light.power.write(1)
    
#        open_valve()
#        time.sleep(1)
#        close_valve()

class SolValPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Solenoid Valves", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        #button3 = tk.Button(self, text="Run Solenoid Valves", command = SolValves)
        #button3.pack()

        button2 = tk.Button(self, text="Components",                         
                            command = lambda: controller.show_frame(ComponentsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home",                        
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()






#where code starts running(i think)
app = MainClass()
app.mainloop()



