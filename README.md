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
 
## Camera
 ### Camera_Terminal_Test_Code.py
 - Contains the code that allows us to take pictures with the camera and save it as a file.
 - Also can create a new directory for the storage of the pictures.
 ### Camera_Code.py
 - Contains the functions used to take a picture during the cleaning process and the code to control it using the camera component page of the GUI.
 
# Setup Raspberry Pi
(Steps 1-4) Standard updates: 
1. `sudo apt-get update`
2. `sudo apt-get upgrade` 
3. `sudo apt-get install python3-pip`
4. `sudo pip3 install --upgrade setuptools`

(Steps 5-8) For installing board (https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi):

5. `cd ~`
6. `sudo pip3 install --upgrade adafruit-python-shell`
7. `wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py`
8. `sudo python3 raspi-blinka.py`

   8a. To check if blinka is installed, enter: `ls /dev/i2c* /dev/spi*`
       You should see the response: 
       `/dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1`

(Steps 11-12 )For installing Linear Actuator: 
11. `python -m pip install PyYAML`
12. Follow instructions on: https://www.pololu.com/docs/0J71/3.1

13. Installing adafruit motor hat library: `sudo pip3 install adafruit-circuitpython-motorkit`
14. Installing automation hat library: `curl https://get.pimoroni.com/automationhat | bash`
