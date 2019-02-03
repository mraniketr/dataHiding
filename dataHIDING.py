import os #to run system commands
import shutil  #to make archive
from tkinter import filedialog
from tkinter import *
import sys #to know the os

def zunz(args):
    if(args==2):
        if(sys.platform=='win32'):
            os.system('rename final2.jpg final2.zip')
            os.system('unzip final2.zip')
        else:
            os.system("unzip final2.jpg") 
       	print("Unzipping sucessful")
   
    elif(args==1):
       #keep a image of file name final.jpg
        root=Tk()
        root.update()
        shutil.make_archive('final','zip',root_dir=filedialog.askdirectory(title = "Open directory containg your files"),base_dir=None)
        root.destroy()
        if(sys.platform=='win32'):
            os.system("copy /b final.jpg+final.zip final2.jpg")
            os.system("del final.zip")
        else:
            os.system("cat final.jpg final.zip > final2.jpg") #to create .jpg with our data
            os.system("rm final.zip") #delete the .zip file 
       
        print("zip created sucessfully")

    else:
        print("Invalid IP")
                

print("1. Make Zip \n2.Unzip") 
if(int(input())==1):
    zunz(1)
else:
    zunz(2)
