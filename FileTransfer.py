import os
import shutil
import sys
import time
import datetime as dt
now = dt.datetime.now()
TODAY= now.today()

File_Extensions = (".png", ".jpg", ".pdf", ".txt", ".mp4", ".mov", ".mp3")

while True:  # mainloop
    welcome_msg = print(f"Welcome to CopyBot! \nToday is {TODAY.strftime('%A, %B the %dth')}")
    pq = input("Do you want to proceed with the copy process?").lower()
    if pq in ("no", "n"):
        sys.exit()

    if pq in ("yes", "y"):
        sourcepath = input("where do you want to copy files from?") # asking the user for the file/picture location
        sourcefiles = os.listdir(sourcepath)
        print(sourcefiles) # listing the files in the directory location
        destinationpath = input("where do you want to send the files?") # asking the user where do they want the pictures?

        for file in sourcefiles:
            if file.endswith(File_Extensions):
                shutil.copy(os.path.join(sourcepath, file), os.path.join(destinationpath, file))
                print("Copying File...")


        time.sleep(1)
        print("Files have been copied! ")  # confirmation that files have copied

        print(os.listdir(destinationpath)) # showing files have been transferred and then looping back to the top
        time.sleep(5)

