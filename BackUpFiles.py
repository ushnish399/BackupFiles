import os
import shutil
source=input("enter the directory to be backed up")
destination=input("enter the directory to be backed up")
ListofFiles=os.listdir(source)
for file in ListofFiles:
    shutil.copy((source+file), destination)