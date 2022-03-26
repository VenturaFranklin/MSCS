import os
import datetime as dt


def before_pic(slide_num, Before_After):
  if Before_After is False:               #Check if the picture taken is the before or after cleaning picture
    pic_order = 'Before_';
  elif Before_After is True:
    pic_order = 'After_';
  pic_directory = '/home/pi/MSCS_Pics/';  #Directory to save the pictures in
  current_date = dt.date.today()          #Gets the current date
  date = str(current_date);               #Turns the current date into a string variable for the picture filename
  file_type = '.jpg';                     #String for the picture file type   
  st_Slide_num = '_' + str(Slide_num);    #Convert the slide number into a string
  Filename = pic_directory + current_date + pic_order + st_Slide_num + file_type    #Path and file name for the picture to be used in the take picture command
  os.system("libcamera-still -t 1000 -o " +Filename)  #System Command to take a picture with the camera
