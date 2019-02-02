import os
import shutil


def zunz(args):
        if(args==2):
                print("Unzipping")
                os.system("unzip final2.jpg")
        else:
 #root_dir = directory of your folder containing secret files
                shutil.make_archive('final','zip',root_dir='/home/aniket/Desktop/Test/Python/Python Project/image hiding/FINAL/DATA',base_dir=None)
                print("zip created sucessfully")
                os.system("cat final.jpg final.zip > final2.jpg") 
                

print("1. Make Zip \n2.Unzip") 
if(int(input())==0):
    zunz(1)
else:
    zunz(2)
