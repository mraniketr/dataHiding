#to run system commands
import os
#to make archive
import shutil
#Filedialog for selection
from tkinter import *
from tkinter import filedialog
#to distinguish between OS
import sys


#function to unzip the encrypted image with classified information
def fuzip():
    if(sys.platform=='win32'):
        os.system('rename classified.jpg classified.rar')
        os.system('7z.exe x classified.rar')
    else:
        os.system("unzip classified.jpg")
    print("Extraction successful")

#function to create zip and the encrypted image with classified information   
def fzip():
    root=Tk()
    root.update()
    shutil.make_archive('final','zip',root_dir=filedialog.askdirectory(title = "Open directory containg your files"),base_dir=None)
    root.destroy()

    if(sys.platform=='win32'):
        isrc=filedialog.askopenfilename()
        os.rename(isrc,'final.jpg')
        os.system("copy /b final.jpg+final.zip classified.jpg")
        os.system("del final.zip")
        os.system("del final.jpg")

    else:
        isrc=filedialog.askopenfilename()
        os.rename(isrc,'final.jpg')
        os.system("cat final.jpg final.zip > classified.jpg")
        os.system("rm final.zip")
    print("Encryption successful")

print("\n1. Create classified image \n2. Extract Data \n")
if(int(input())==1):
    fzip()
else:
    fuzip()
