import os
import shutil

#root_dir = directory of your folder containing secret files
shutil.make_archive('final','zip',root_dir='/home/aniket/Desktop/Test/Python/Python Project/image hiding/FINAL/DATA',base_dir=None)

print("zip created sucessfully")

os.system("cat final.jpg final.zip > final.jpg")

print("Unzipping")
os.system("unzip final.jpg")
