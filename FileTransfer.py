import os
import shutil
import glob
import time
import sys
from os import path

OSquestion = input("Are you on Mac, linux or Windows?").lower()

if OSquestion == "windows":
    usersdirectory = os.chdir(r"C:\Users") # move to the users directory in the C drive if on windows
    print(os.listdir(usersdirectory))

if OSquestion == "mac" or OSquestion == "linux": # move to the users directory /Users if on MacOS or linux
    usersdirectory = os.chdir(r"/Users")
    print(os.listdir(usersdirectory))
else:
    print("please type windows or mac or linux.")


while True:  # mainloop
    pq = input("Do you want to proceed?").lower()
    if pq == "no" or pq == "y":
        continue

    if pq == "yes" or pq == "y":
        sourcepath = input("where do you want to copy files from?") # asking the user for the file/picture location
        sourcefiles = os.listdir(sourcepath)
        print(sourcefiles) # listing the files in the directory location
        destinationpath = input("where do you want to send the files?") # asking the user where do they want the pictures?

#  the code that transfers files
#  if files end in common file extensions then move them to the desired users location
    for file in sourcefiles:
         if file.endswith(".png"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith(".jpg"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".pdf"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".txt"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".mp4"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".mov"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".mp4"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".mp3"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".txt"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
# accounting for capitalized file extensions for some random reason.
    for file in sourcefiles:
         if file.endswith( ".MOV"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".JPG"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".MP4"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".MP3"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".PNG"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".PDF"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
    for file in sourcefiles:
         if file.endswith( ".TXT"):
             shutil.copy(os.path.join(sourcepath,file), os.path.join(destinationpath,file))


    print(os.listdir(destinationpath)) # showing files have been transferred and then looping back to the top


    # commented out testing
    # confirmationQ = input("Have the files been copied? ").lower()  # confirmation that files have copied
    # if confirmationQ == "yes":
    #     break
    # if confirmationQ ==
