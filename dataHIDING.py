import os
import shutil
from tkinter import filedialog
from tkinter import *



def zunz(args):
    if(args==2):
        print("Unzipping")
        os.system("unzip final2.jpg")
 #root_dir = directory of your folder containing secret files
 #d='/home/aniket/Desktop/Test/Python/Python Project/image hiding/FINAL/DATA'
    else:
        root=Tk() #Tk window to hold the button:
        root.update()
        shutil.make_archive('final','zip',root_dir=filedialog.askdirectory(),base_dir=None)
        root.destroy()
        print("zip created sucessfully")
        os.system("cat final.jpg final.zip > final2.jpg") 
                

print("1. Make Zip \n2.Unzip") 
if(int(input())==1):
    zunz(1)
else:
    zunz(2)
