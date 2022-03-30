#Created by Elijah Keeswood on 03/08/2022
#Copyright @ 2022 Elijah Keeswood. All rights reserved.
#Senior Design Team: 22010
#MSCS GUI

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

#Variables
LARGE_FONT = ("Verdana", 20)
MED_FONT = ("Calibri", 15)
pic_num = 0


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

        for F in (StartPage, ComponentsPage, RollersPage, LinActPage, PumpsPage, SolValPage, CameraPage):      
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
# def stopMrClean():
#     exit(mrClean)
#     stopSoap()
#     stopRollers()
#     stopWater()
#     closeAir()
#     turnoffAll_valves()
#     gotoTop()
#     print("stopped cleaning")
#     
# def stopCleanWin():
#     
#     stopPopup = tk.Tk()
#     stopPopup.title("Cleaning Initiated")
#     button = tk.Button(stopPopup, text = "Stop Cleaning", width=10, height=10, command = stopMrClean)
#     button.pack()
#     stopPopup.mainloop()


def mrClean():
    #stopCleanWin() #popup window for stop button
    # print ("Go to Home")
    # gotoHome()#calling to function in ticControl.py
    global pic_num
    
    print("take 'before' picture")
    pic_num += 1 #Increases the count number for next image 
    Camera_Code.Take_Pic(pic_num, False) #Camera Takes picture and sends as False to name as "before"

    print("Start Rollers")
    StartStopRollers.startRollers() #Starts Rollers
    
    print("Dispense Reagent")
    DispenseReagent.startSoap() #Dispenses soap
    time.sleep(5)
    DispenseReagent.stopSoap() #stops dispensing soap
   
    print("Go to Home")
    ticControl.gotoHome() #Linear Actuator moves slide to home position or cleaning position

    print("CLEAN OSCILLATE")
    ticControl.oscClean() #Linear Actuator oscillates slide up and down between the rollers

    print("Rollers off")
    StartStopRollers.stopRollers() #stops rollers
  
    print("Rinse")
    WaterPump.startWater() #Dispenses Water
    time.sleep(3)
    WaterPump.stopWater() #stops dispensing water
    
    print("Open Air")
    OpenCloseAir.open_air() #Opens the drying air valve

    print("DRYING OSCILLATE")
    ticControl.oscDry() #Linear Actuator moves slide up slowly between the drying air nozzles
    
    print("close air")
    OpenCloseAir.close_air() #Closes drying air valve
    
    print("go to Top")
    ticControl.gotoTop() #Linear Actuator moves slide up to top

    print("take 'after' picture")
    Camera_Code.Take_Pic(pic_num, True) #Camera Takes picture and sends as True to name as "after"
    
    print("done")



def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/") #opens and displays file explorer
      

def main_exit_handler():
    print("exiting")

class StartPage(tk.Frame):                                 #The Start Page. tk.Frame inherits so we don't have to call.
    def __init__(self, parent, controller):
        print("registering exit handler")
        atexit.register(main_exit_handler)
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MSCS Main Page", font = LARGE_FONT) #class is tk.label() which creates the object = label. 
                                                             #LARGE_FONT defined at the top
        label.pack(pady=10, padx=10) #pad puts padding on it. looks nice.

        button1 = tk.Button(self, text="CLEAN", width =30, height=7, font=MED_FONT, command = mrClean)
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

        button5 = tk.Button(self, text="Camera", width =20, height=5, font=MED_FONT,
                            command=lambda: controller.show_frame(CameraPage))
        button5.pack()

        button1 = tk.Button(self, text="Back to Home",                          #doesn't matter what button variable is called. its unique to class
                            command = lambda: controller.show_frame(StartPage)) 
        button1.pack()


class RollersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Rollers", font = LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        #start rollers
        button3 = tk.Button(self, text="Start", width =20, height=5, command = StartStopRollers.startRollers)
        button3.pack()
        #stop rollers
        button4 = tk.Button(self, text="Stop", width =20, height=5, command = StartStopRollers.stopRollers)
        button4.pack()

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

        button3 = tk.Button(self, text="Calibrate", width =20, height=5, command = ticControl.calibrate)
        button3.pack()
        #start
        button4 = tk.Button(self, text="Start", width =20, height=5, command = ticControl.start)
        button4.pack()
        #up
        button5 = tk.Button(self, text="Up", width =20, height=5, command = ticControl.up)
        button5.pack()
        #down
        button6 = tk.Button(self, text="Down", width =20, height=5, command = ticControl.down)
        button6.pack()

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
        
        button4 = tk.Button(self, text="Start Soap", command = DispenseReagent.startSoap)
        button4.pack()
        
        button5 = tk.Button(self, text="Stop Soap", command = DispenseReagent.stopSoap)
        button5.pack()

        button6 = tk.Button(self, text="Start Water", command = WaterPump.startWater)
        button6.pack()
        
        button6 = tk.Button(self, text="Stop Water", command = WaterPump.stopWater)
        button6.pack()

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

        button3 = tk.Button(self, text="Open Air", command = OpenCloseAir.open_air)
        button3.pack()
        
        button4 = tk.Button(self, text="Close Air", command = OpenCloseAir.close_air)
        button4.pack()
        
        button5 = tk.Button(self, text="Open Gripper", command = OpenCloseAir.open_gripper)
        button5.pack()

        button6 = tk.Button(self, text="Close Gripper", command = OpenCloseAir.close_gripper)
        button6.pack()
        
        button7 = tk.Button(self, text="Turn Off All Valves", command = OpenCloseAir.turnoffAll_valves)
        button7.pack()

        button2 = tk.Button(self, text="Back to Pumps",                         
                            command = lambda: controller.show_frame(PumpsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home",                        
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

class CameraPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Camera", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button3 = tk.Button(self, text="Take Picture", command = Camera_Code.Take_Test_Pic) #Takes test image labelled as test
        button3.pack()

        button4 = tk.Button(self, text="Files", width =20, height=5, font=MED_FONT, command = browseFiles)
        button4.pack()

        button2 = tk.Button(self, text="Back to Components",                         
                            command = lambda: controller.show_frame(ComponentsPage))
        button2.pack()

        button1 = tk.Button(self, text="Back to Home",                        
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()




#where code starts running
app = MainClass()
app.geometry ("1000x500") #width x height of window
app.mainloop()

#closes air valves after exiting/shutting down main 
print("Turning off All valves")
OpenCloseAir.turnoffAll_valves()



