import os
import datetime as dt

current_date = dt.date.today()
i = 'n';
date = str(current_date);
file_type = '.jpg';
pic_num = 1;
#print("Current Working Directory: {0}".format(os.getcwd()));

o_path = format(os.getcwd())

make = input("Would you like to make a new folder (y,n)?");

if make == 'y':
    os.mkdir(date);

new_path = o_path + '/' + date;
#print("Current Path is:" +new_path);
os.chdir(new_path);
#print("Current Working Directory: {0}".format(os.getcwd()));

while (i!='y'):
    st_pic_num = str(pic_num);
    Filename = st_pic_num + file_type
    choice = input("Do you want to take a picture (Y/N)?");
    if choice in ['y', 'Y']:
        os.system("libcamera-still -t 1000 -o " +Filename)
        pic_num += 1;
    else:
        print("No image was captured");
    #print("The Date is: ", current_date);
    i = input("Do you want to quit (y,n)?");