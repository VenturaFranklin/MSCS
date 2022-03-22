# MSCS

This folder contains all files of code needed to run the GUI and control all the components for the MSCS 

# File Descriptions

## GUI
 ### MSCS_GUI.py
 - GUI code without implemented hardware functions. This code the same as MSCS_GUI_1.py but with the hardware functions commented out. This is used for only testing  GUI related functions.
 ### MSCS_GUI_1.py
 - Working GUI code with implemented hardware functions. This is used to run the automated cleaning cycle and also individually control the rest of components. 


## DC motors
 ### StartStopRollers.py
 - Contains the functions for starting and stopping the dc motors/cleaning rollers. 
 - Functions are called to automatically in the cleaning cycle and manually in the Rollers page. 
 
 
## Linear Actuator 
 ### LASettings.yaml
 - Linear actuator location settings.
 ### tic_settings.txt
 - Pololu Tic USB Stepper Controller settings file.
 ### ticControl.py
 - Contains the functions used to control the movement and placements of the linear actuator.
 - Functions are called to automatically in the cleaning cycle and manually in the Linear Actuator page.


## Pumps
 ### DispenseReagent.py
 - Controls the pump for the soap. 
 - Functions are called to automatically in the cleaning cycle and manually in the Pumps page. 
 ### WaterPump.py
 -  Controls the pump for the water. 
 -  Functions are called to automatically in the cleaning cycle and manually in the Pumps page.


## Solenoid Valves
 ### OpenCloseAir.py
 - Contains the functions for turning on and off relays 1 2 and 3 on automation hat. Controls the opening and closing of solenoid valves. 
 - Relay one is for opening and closing drying valve. Relays two and three are for the valves that open and close the gripper. 
 - Functions are called to automatically in the cleaning cycle and manually in the Solenoid Valves page.
 

## pin assignments
 - Variable assignments for Raspberry Pi pin numbers
 
