import os
import shutil
from tkinter import filedialog
from tkinter import *

def zunz(args):
    if(args==2):
        print("Unzipping")
        os.system("unzip final2.jpg")
    elif(args==1):
        root=Tk() #Tk window to hold the button:
        root.update()
        shutil.make_archive('final','zip',root_dir=filedialog.askdirectory(title = "Open directory containg your files"),base_dir=None)
        root.destroy()
        print("zip created sucessfully")
        os.system("cat final.jpg final.zip > final2.jpg") 
        os.system("rm final.zip") 
    else:
        print("Invalid IP")
                

print("1. Make Zip \n2.Unzip") 
if(int(input())==1):
    zunz(1)
else:
    zunz(2)
