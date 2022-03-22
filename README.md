# MSCS

This folder contains all files of code needed to run the GUI and control all the components for the MSCS 

# File Descriptions

## DC motors
 ### dcmotorcontrollerexample.py
 - 
 ### StartStopRollers.py
 - Contains the functions for starting and stopping the dc motors/cleaning rollers. 
 - Get called to automatically in the cleaning cycle and manually in the Rollers page. 
 ### testspace.py
 - Test code for dc motors

## Pumps
 ### DispenseReagent.py
 - Soap
 ### File Name: WaterPump.py
 - Description: 
 
## Linear Actuator 
 ### LASettings.yaml
 - Description: 
 ### tic_settings.txt
 - Pololu Tic USB Stepper Controller settings file.
## ticControl.py
 - Description: 

## pin assignments
 - Variable assignemtns for Raspberry Pi pin numbers

## Solenoid Valves
 ### OpenCloseAir.py
 - Code for turning on and off relays 1 2 and 3 on automation hat. Controls the opening and closing of solenoid valves. 
 - Relay one is for the drying valve. Relays two and three are for the valves that open and close the gripper. 
 ### solenoidvalvetest.py
 - Test code for turning on and off relay one.
 
## GUI
 ### MSCS_GUI.py
 - GUI code without implemented hardware functions. This code the same as MSCS_GUI_1.py but with the hardware functions commented out. This is used for only testing  GUI related functions.
 ### MSCS_GUI_1.py
 - Working GUI code with implemented hardware functions. This is used to run the automated cleaning cycle and also individually control the rest of components. 
 - So far it can run 

