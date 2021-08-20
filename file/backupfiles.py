import os
import shutil

source=input("enter stuff")
destination=input("enter distination folder name :|")
source=source+'/'
destination=destination+'/'
list_of_files=os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file),destination)