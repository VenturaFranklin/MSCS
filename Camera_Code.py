#Created by Dayton Brown
#Senior Design Team 22010
#Camera Code 

import os
import datetime as dt
import time

def Take_Pic(slide_num, Before_After):    #Function to take the before and after cleaning pics
  #time.sleep(10) #Used for testing call to fxn in GUI. Probably just delete.
  #return #this was for testing too
  if Before_After is False:               #Check if the picture taken is the before or after cleaning picture
    pic_order = 'Before_';
    #os.system("v4l2-ctl -c focus_abslute=570")
    #The line above sets what the camera is focused on. Currently waiting on testing to determine the numerical value.
  else:
    pic_order = 'After_';
  pic_directory = '/home/pi/MSCS_Pics/';  #Directory to save the pictures in
  current_date = dt.date.today()          #Gets the current date
  date = str(current_date);               #Turns the current date into a string variable for the picture filename
  file_type = '.jpg';                     #String for the picture file type   
  st_Slide_num = '_' + str(slide_num);    #Convert the slide number into a string
  Filename = pic_directory + date + pic_order + st_Slide_num + file_type    #Path and file name for the picture to be used in the take picture command
  os.system("libcamera-still -t 1000 -o " +Filename)  #System Command to take a picture with the camera

def Take_Test_Pic():
  pic_directory = '/home/pi/MSCS_Pics/';  #Directory to save the pictures in
  file_name_type = 'test.jpg';            #String for the picture file name
  Filename_path = pic_directory  + file_name_type #Path and file name for take picture commanf
  os.system("libcamera-still -t 1000 -o " +Filename_path) #System Command to take a picture with the camera
