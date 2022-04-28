#Created by Elijah Keeswood on 03/08/2022
#Senior Design Team: 22010
#MSCS GUI

import threading
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

#Accesses separate files in same folder and imports the file's imports
import ticControl 
import StartStopRollers 
import DispenseReagent
import WaterPump
import OpenCloseAir 
import Camera_Code
import math

running = True

#Variables
LARGE_FONT = ("Verdana", 40)
MED_FONT = ("Calibri", 30)
SMALL_FONT= ("Calibri", 20)
pic_num = 0
mainthread = None

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

        for F in (StartPage, ComponentsPage, RollersPage, LinActPage, PumpsPage, SolValPage, CameraPage, ExitPage):      
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
def stopMrClean(message):
    global running
    running = False
    DispenseReagent.stopSoap()
    StartStopRollers.stopRollers()
    WaterPump.stopWater()
    OpenCloseAir.close_air()
    OpenCloseAir.turnoffAll_valves()
    ticControl.gotoHome() # don't move the linear actuator
    message.set("stopped all processess")
    
#     
# def stopCleanWin():
#     
#     stopPopup = tk.Tk()
#     stopPopup.title("Cleaning Initiated")
#     button = tk.Button(stopPopup, text = "Stop Cleaning", width=10, height=10, command = stopMrClean)
#     button.pack()
#     stopPopup.mainloop()

def mrCleanThread(message):
    mainthread = threading.Thread(target = mrClean, args = (message,))
    mainthread.start()
    errorThread = threading.Thread(target = errorHandler, args = (message,), daemon=True)
    errorThread.start()
    

# this function is the thread that watches for linear actuator errors, in case of error,
# the cleaning process should be stopped
def errorHandler(message):
    global running
    print("main error thread started")
    while True:
        if running == False:
            return
        if ticControl.hasError():
            print("error detected")
            # houston we have a problem
            message.set("Error Detected, Stopping System")
            stopMrClean(message)
            
        time.sleep(0.1)
# def errorMessage();
#     message.set()

def mrClean(message):
    global pic_num
    global running

    running = True

    if not running:
        return

    #stopCleanWin() #popup window for stop button

    try:
#         if running:
#             message.set("take 'before' picture")
#             pic_num += 1 #Increases the count number for next image 
#             Camera_Code.Take_Pic(pic_num, False) #Camera Takes picture and sends as False to name as "before"
        ticControl.onStart()
        if running:
            message.set("Start Rollers")
            StartStopRollers.startRollers() #Starts Rollers
        if running:
            message.set("Dispense Reagent")
            DispenseReagent.startSoap() #Dispenses soap
            time.sleep(1)
            DispenseReagent.stopSoap() #stops dispensing soap
        if running:
            message.set("Go to Home")
            ticControl.gotoHome() #Linear Actuator moves slide to home position or cleaning position

        if running:
            message.set("CLEAN OSCILLATE")
            #Linear Actuator oscillates slide up and down between the rollers
            numiter = 3
            toppos = 16250
            bottom = 5600
            currpos = toppos
            dist = math.ceil((toppos - bottom) / numiter)
            for i in range(numiter):
                if running:
                    ticControl.goto(bottom)
                if running:
                    if i == numiter - 1:
                        WaterPump.startWater()
                        break
                    ticControl.goto(toppos)
#                 ticControl.goto(currpos - dist)
#                 ticControl.goto(currpos - math.ceil(dist / 2))
#                 currpos = currpos - dist

        if running:
            ticControl.gotoHome()#goes to home position above rollers
            WaterPump.stopWater() #stops dispensing water
        if running:
            message.set("Rollers off")
            StartStopRollers.stopRollers() #stops rollers
        if running:    
            message.set("Open Air")
            OpenCloseAir.open_air() #Opens the drying air valve
        if running:
            message.set("DRYING OSCILLATE")
            ticControl.oscDry() #Linear Actuator moves slide up slowly between the drying air nozzles
        if running:    
            message.set("close air")
            OpenCloseAir.close_air() #Closes drying air valve
            
            message.set("Go to Home")
            ticControl.gotoHome() #Linear Actuator moves slide up to top
            message.set("Done Cleaning")

#         print("take 'after' picture")
#         Camera_Code.Take_Pic(pic_num, True) #Camera Takes picture and sends as True to name as "after"
        
        
    
    # in case an error is thrown, do this
    except:
        print("error thrown")
        
    # then after code is run, no matter what, do this. i.e stop all systems
    finally:
        print("finished running ")
        running = True
        message.set("Resetting Components")
        print("Resetting Components")
        time.sleep(2)
        message.set("Click Clean to Start")



def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/") #opens and displays file explorer
    
def Prime(message):
    message.set("Priming")
    DispenseReagent.startSoap()
    WaterPump.startWater()
    time.sleep(3)
    DispenseReagent.stopSoap()
    WaterPump.stopWater()
    message.set("Done Priming")
    message.set("Click Clean to Start")
    
    
    
    
    
    
    
    
    

class StartPage(tk.Frame):                                 #The Start Page. tk.Frame inherits so we don't have to call.
    def __init__(self, parent, controller):
        global running

        tk.Frame.__init__(self, parent)


        label = tk.Label(self, text="MSCS Main Page", font = LARGE_FONT) #class is tk.label() which creates the object = label. 
                                                             #LARGE_FONT defined at the top
        label.grid(row=0, column=2) 


        message = tk.StringVar()   
        mess = tk.Label(self, textvariable=message, font = MED_FONT) 
        mess.grid(row=1, column=2)
                            
    
        button1 = tk.Button(self, text="CLEAN", width =15, height=5, font=LARGE_FONT, command = lambda: mrCleanThread(message))
        button1.grid(row=3, column=2, padx=50)
        
        button3 = tk.Button(self, text="STOP", width =15, height=5, font=MED_FONT, command = lambda: stopMrClean(message))
        button3.grid(row=4, column=2)
        
        running = True #Reads through buttons on start up it. This makes it so does not stay running=False from stopMrClean
        

        button5 = tk.Button(self, text="Open\nGripper", width=10, height=5, font=MED_FONT, command = OpenCloseAir.open_gripper)
        button5.grid(row=3, column=4, padx=10, pady=50)

        button6 = tk.Button(self, text="Close\nGripper", width=10, height=5, font=MED_FONT, command = OpenCloseAir.close_gripper)
        button6.grid(row=4, column=4)


        button2 = tk.Button(self, text="Components", width=15, height=6, font=MED_FONT,
                            command = lambda: controller.show_frame(ComponentsPage)) 
                                     #lambda creates a quick throwaway fxn. Only here when we call it.
                                     #can also pass variables through; command = lambda: fxn("sus")
                                                                   #ComponentsPage is a class                        
        button2.grid(row=3, column=1, padx=50, sticky='s')
        
        button4 = tk.Button(self, text="Files", width =10, height=3, font=MED_FONT, command = browseFiles) #calls to browse files explorer
        button4.grid(row=4, column=1)

        button7 = tk.Button(self, text="Exit", width =7, height=1, font=MED_FONT, command = lambda: controller.show_frame(ExitPage)) #Exits the MSCS GUI window
        button7.grid(row=1, column=5, sticky='ne')        
        
        button7 = tk.Button(self, text="Prime", width =10, height=3, font=MED_FONT, command = Prime(message)) #Exits the MSCS GUI window
        button7.grid(row=3, column=5, padx=20, sticky='s')  

        message.set("Click Clean to Start")  


class ComponentsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Components", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="Rollers", width =15, height=2,font=MED_FONT,
                            command=lambda: controller.show_frame(RollersPage))
        button2.pack()

        button3= tk.Button(self, text="Linear Actuator",width =15, height=2, font=MED_FONT,
                            command=lambda: controller.show_frame(LinActPage))
        button3.pack()

        button6 = tk.Button(self, text="Solenoid Valves",width=15, height=2, font=MED_FONT,                       
                            command = lambda: controller.show_frame(SolValPage))
        button6.pack()

        button4 = tk.Button(self, text="Pumps", width =15, height=2, font=MED_FONT,
                            command=lambda: controller.show_frame(PumpsPage))
        button4.pack()

        button5 = tk.Button(self, text="Camera", width =15, height=2, font=MED_FONT,
                            command=lambda: controller.show_frame(CameraPage))
        button5.pack()
        
        button1 = tk.Button(self, text="Back to Home", width=15, height=2, font=SMALL_FONT,  #doesn't matter what button variable is called. its unique to class
                            command = lambda: controller.show_frame(StartPage)) 
        button1.pack()


class RollersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Rollers", font = LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        #start rollers
        button3 = tk.Button(self, text="Start", width =20, height=5, font=MED_FONT, command = StartStopRollers.startRollers)
        button3.pack()
        #stop rollers
        button4 = tk.Button(self, text="Stop", width =20, height=5, font=MED_FONT, command = StartStopRollers.stopRollers)
        button4.pack()

        button2 = tk.Button(self, text="Components",  width=20, height=3, font=SMALL_FONT,                     
                            command = lambda: controller.show_frame(ComponentsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home", width=15, height=3, font=SMALL_FONT,                        
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

class LinActPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Linear Actuator", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button3 = tk.Button(self, text="Calibrate", width =20, height=2, font=MED_FONT, command = ticControl.calibrate)
        button3.pack()
        #start
        button4 = tk.Button(self, text="Start", width =20, height=2, font=MED_FONT, command = ticControl.start)
        button4.pack()
        #up
        button5 = tk.Button(self, text="Up", width =20, height=2, font=MED_FONT, command = ticControl.up)
        button5.pack()
        #down
        button6 = tk.Button(self, text="Down", width =20, height=2, font=MED_FONT, command = ticControl.down)
        button6.pack()

        button2 = tk.Button(self, text="Back to Components", width=20, height=2, font=SMALL_FONT,                       
                            command = lambda: controller.show_frame(ComponentsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home", width=15, height=2, font=SMALL_FONT,         
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

class PumpsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Pumps", font = LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button4 = tk.Button(self, text="Start Soap", width =20, height=2, font=MED_FONT, command = DispenseReagent.startSoap)
        button4.pack()
        
        button5 = tk.Button(self, text="Stop Soap", width =20, height=2, font=MED_FONT, command = DispenseReagent.stopSoap)
        button5.pack()

        button6 = tk.Button(self, text="Start Water", width =20, height=2, font=MED_FONT, command = WaterPump.startWater)
        button6.pack()
        
        button6 = tk.Button(self, text="Stop Water", width =20, height=2, font=MED_FONT, command = WaterPump.stopWater)
        button6.pack()

        button2 = tk.Button(self, text="Back to Components", width=20, height=2, font=SMALL_FONT,                        
                            command = lambda: controller.show_frame(ComponentsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home", width=15, height=2, font=SMALL_FONT,                       
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()


class SolValPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Solenoid Valves", font = LARGE_FONT)
        label.grid(row=0, column=2, pady=10, padx=10)
        label = tk.Label(self, text = "\t      ", font = MED_FONT)
        label.grid(column=0)

        button3 = tk.Button(self, text="Open Air", width =15, height=2, font=MED_FONT, command = OpenCloseAir.open_air)
        button3.grid(row=1, column=1, sticky='e')
        
        button4 = tk.Button(self, text="Close Air", width =15, height=2, font=MED_FONT, command = OpenCloseAir.close_air)
        button4.grid(row=2, column=1, sticky='e')
        
        button5 = tk.Button(self, text="Open Gripper", width =15, height=2, font=MED_FONT, command = OpenCloseAir.open_gripper)
        button5.grid(row=1, column=3, sticky='w')

        button6 = tk.Button(self, text="Close Gripper", width =15, height=2, font=MED_FONT, command = OpenCloseAir.close_gripper)
        button6.grid(row=2, column=3, sticky='w')
        
        button7 = tk.Button(self, text="Turn Off All Valves", width =18, height=2, font=MED_FONT, command = OpenCloseAir.turnoffAll_valves)
        button7.grid(row=3, column=2, sticky='n')

        button2 = tk.Button(self, text="Back to Components", width=20, height=2, font=SMALL_FONT,                         
                            command = lambda: controller.show_frame(ComponentsPage))
        button2.grid(row=4, column=2)

        button1 = tk.Button(self, text="Back to Home",  width=15, height=2, font=SMALL_FONT,                       
                            command = lambda: controller.show_frame(StartPage))
        button1.grid(row=5, column=2)

class CameraPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Camera", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button3 = tk.Button(self, text="Take Picture", width =20, height=5, font=MED_FONT, command = Camera_Code.Take_Test_Pic) #Takes test image labelled as test
        button3.pack()

        button4 = tk.Button(self, text="Files", width =20, height=3, font=MED_FONT, command = browseFiles)
        button4.pack()

        button2 = tk.Button(self, text="Back to Components", width=20, height=3, font=SMALL_FONT,                        
                            command = lambda: controller.show_frame(ComponentsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home", width=15, height=3, font=SMALL_FONT,                        
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()
        
class ExitPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "EXIT\nAre you sure?", font = LARGE_FONT)
        label.pack(pady=10, padx=10)      
        button4 = tk.Button(self, text="Yes", width =15, height=3, font=MED_FONT, command = controller.destroy)
        button4.pack(pady=10)
        button4 = tk.Button(self, text="No", width =15, height=3, font=MED_FONT, command = lambda: controller.show_frame(StartPage))
        button4.pack(pady=10)  

#where code starts running
app=MainClass()
#app.geometry("800x800") #width x height of window
app.attributes('-fullscreen', True)
app.mainloop()

#closes air valves after exiting/shutting down main 
print("Turning off All valves")
OpenCloseAir.turnoffAll_valves()
