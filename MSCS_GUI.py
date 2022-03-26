#Created by Elijah Keeswood on 03/08/2022
#Copyright @ 2022 Elijah Keeswood. All rights reserved.
#Senior Design Team: 22010
#MSCS GUI MK1

import sys
from multiprocessing import Process
from threading import Thread

#Import tkinter library
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog #For accessing computers files

#Imports for Raspberry Pi
import time
from tracemalloc import start
from turtle import up
import atexit

#import board
#from adafruit_motorkit import MotorKit
#import RPi.GPIO as GPIO

##Imports for Automation Hat
#import automationhat
#import RPi.GPIO as io
#from time import sleep

# #Accesses separate files in same folder and imports the file's imports
# from ticControl import * #linear Actuator
# from StartStopRollers import *
# from DispenseReagent import * 
# from WaterPump import * 
# from OpenCloseAir import * 

#Variables
LARGE_FONT = ("Verdana", 20)
MED_FONT = ("Calibri", 15)



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
def startBothCleanFxns():
    if __name__=='__main__':
        p1 = Process(target = stopCleanWin)
        p1.start()
        p2 = Process(target = mrClean)
        p2.start()

def stopMrClean():
    return(mrClean)
    # stopSoap()
    # stopRollers()
    # stopWater()
    # closeAir()
    # turnoffAll_valves()
    # gotoTop()
    # print("stopped cleaning")
    
def stopCleanWin():
    stopPopup = tk.Tk()
    stopPopup.title("Cleaning Initiated")
    button = tk.Button(stopPopup, text = "Stop Cleaning", width=10, height=5, command = stopMrClean)
    button.pack()
    stopPopup.mainloop()

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

def mrClean():
    print("cleaning")
    countdown(10)
    #time.sleep(10)
    print("stop cleaning")
    #print ("Go to Home")
    # start linear actuator 
    # gotoHome()#calling to function in ticControl.py
   
    # print("take picture")
    # print("Start Rollers")
    # startRollers() #calling to fxn in StartRollers.py
    
    # print("Dispense Reagent")
    # dispenseSoap() #calling to fxn in DispenseReagents.py
    # time.sleep(5)
    # stopSoap()
   
    # print("Go to Home")
    # gotoHome() #call to ticControl.py

    # print("CLEAN OSCILLATE")
    # oscClean() #call to ticControl.py

    # print("Rollers off")
    # stopRollers() #call to StartStopRollers.py
  
    # print("Rinse")
    # startWater()#rinsing fxn from WaterPump.py #can change to just dispenseWater()
    # time.sleep(3)
    # stopWater()
    
    # print("Open Air")
    # open_air() #from OpenCloseAir.py

    # print("DRYING OSCILLATE")
    # oscDry() #from ticControl.py
    
    # print("close air")
    # close_air() #from OpenCloseAir.py
    
    # print("go to Top")
    # gotoTop() #from ticControl.py
    
    # print("done")


def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/") #opens and displays file explorer
      

def main_exit_handler():
    print("exiting")

class StartPage(tk.Frame):                                 #The Start Page. tk.Frame inherits so we don't have to call.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MSCS Main Page", font = LARGE_FONT) #class is tk.label() which creates the object = label. 
                                                             #LARGE_FONT defined at the top
        label.pack(pady=10, padx=10) #pad puts padding on it. looks nice.

        button1 = tk.Button(self, text="CLEAN", width =30, height=7, font=MED_FONT, command = startBothCleanFxns) #popup window for stop button
        button1.pack()
        

        button2 = tk.Button(self, text="Components", width =20, height=6, font=MED_FONT,
                            command = lambda: controller.show_frame(ComponentsPage)) 
                                     #lambda creates a quick throwaway fxn. Only here when we call it.
                                     #can also pass variables through; command = lambda: fxn("sus")
                                                                   #ComponentsPage is a class                        
        button2.pack()
        
        button4 = tk.Button(self, text="Files", width =20, height=5, font=MED_FONT, command = browseFiles) #calls to browse files explorer
        button4.pack()


class ComponentsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Components", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="Rollers", width =20, height=5,font=MED_FONT,
                            command=lambda: controller.show_frame(RollersPage))
        button2.pack()

        button3= tk.Button(self, text="Linear Actuator",width =20, height=5, font=MED_FONT,
                            command=lambda: controller.show_frame(LinActPage))
        button3.pack()

        button4 = tk.Button(self, text="Pumps", width =20, height=5, font=MED_FONT,
                            command=lambda: controller.show_frame(PumpsPage))
        button4.pack()

        button1 = tk.Button(self, text="Back to Home",                          #doesn't matter what button variable is called. its unique to class
                            command = lambda: controller.show_frame(StartPage)) 
        button1.pack()


class RollersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Rollers", font = LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        # #start rollers
        # button3 = tk.Button(self, text="Start", width =20, height=5, command = startRollers)
        # button3.pack()
        # #stop rollers
        # button4 = tk.Button(self, text="Stop", width =20, height=5, command = stopRollers)
        # button4.pack()

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

        # button3 = tk.Button(self, text="Calibrate", width =20, height=5, command = calibrate)
        # button3.pack()
        # #start
        # button4 = tk.Button(self, text="Start", width =20, height=5, command = start)
        # button4.pack()
        # #up
        # button5 = tk.Button(self, text="Up", width =20, height=5, command = up)
        # button5.pack()
        # #down
        # button6 = tk.Button(self, text="Down", width =20, height=5, command = down)
        # button6.pack()


        button2 = tk.Button(self, text="Back to Components",                       
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

        button3 = tk.Button(self, text="Solenoid Valves",width=20, height=5, font=MED_FONT,                       
                            command = lambda: controller.show_frame(SolValPage))
        button3.pack()
        
        # button4 = tk.Button(self, text="Start Soap", command = dispenseSoap)
        # button4.pack()
        
        # button5 = tk.Button(self, text="Stop Soap", command = stopSoap)
        # button5.pack()

        # button6 = tk.Button(self, text="Start Water", command = startWater)
        # button6.pack()
        
        # button6 = tk.Button(self, text="Stop Water", command = stopWater)
        # button6.pack()

        button2 = tk.Button(self, text="Back to Components",                         
                            command = lambda: controller.show_frame(ComponentsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home",                        
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()


class SolValPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Solenoid Valves", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        # button3 = tk.Button(self, text="Open Air", command = open_air)
        # button3.pack()
        
        # button4 = tk.Button(self, text="Close Air", command = close_air)
        # button4.pack()
        
        # button5 = tk.Button(self, text="Open Gripper", command = open_gripper)
        # button5.pack()

        # button6 = tk.Button(self, text="Close Gripper", command = close_gripper)
        # button6.pack()
        
        # button7 = tk.Button(self, text="Turn Off All Valves", command = turnoffAll_valves)
        # button7.pack()

        button2 = tk.Button(self, text="Back to Pumps",                         
                            command = lambda: controller.show_frame(PumpsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home",                        
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()




#where code starts running
app = MainClass()
app.geometry ("1000x500") #width x height of window
app.mainloop()
sys.exit()
# #closes air valves after exiting/shutting down main 
#  atexit.register(main_exit_handler)
# print("Turning off All valves")
# automationhat.relay.one.off()
# automationhat.relay.two.off()
# automationhat.relay.three.off()