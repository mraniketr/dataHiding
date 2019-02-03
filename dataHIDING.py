import os 															#to run system commands
import shutil 			 										    #to make archive
from tkinter import filedialog
from tkinter import *
import sys 															#to know the os for os specific commands

def zunz(args):
    if(args==2):													#Extraction
        if(sys.platform=='win32'):
            os.system('rename classified.jpg classified.zip')
            os.system('unzip classified.zip')
        else:
            os.system("unzip classified.jpg") 
       	print("Extraction successful")
   
    elif(args==1):													#Encryption

   
        root=Tk()
        root.update()
   																	#Creating Zip
        shutil.make_archive('final','zip',root_dir=filedialog.askdirectory(title = "Open directory containg your files"),base_dir=None)
        root.destroy()

        if(sys.platform=='win32'):			
            os.system("copy /b final.jpg+final.zip classified.jpg")		#to create encrypted image
            os.system("del final.zip")								#delete the .zip file
        else:
            os.system("cat final.jpg final.zip > classified.jpg") 		#to create encrypted image
            os.system("rm final.zip") 								#delete the .zip file 
       
        print("Encryption successful")

    else:
        print("Invalid Input")
                

print("\n1. Create classified image \n2. Extract Data \n") 
if(int(input())==1):
    zunz(1)
else:
    zunz(2)
