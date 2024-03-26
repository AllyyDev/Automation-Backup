# first install the schedule module in the terminal

import os
import shutil
import datetime
import schedule
import time

source = "C:/Users/ayoba/OneDrive/Bilder/Screenshots"
# the place of the folder that you want to get the backup data
destination = "C:/Users/ayoba/OneDrive/Desktop/Backup"
# the destination where you want the data to be backed up

def copyFolderTo(source, dest):
    today = datetime.date.today()
    destDir = os.path.join(dest, str(today))
    # variables to state the time and create a path at the destination directory

    try:
        shutil.copytree(source, destDir)
        print(f"folder copied to: {destDir}")
        # copy process
    except FileExistsError:
        print(f"folder already exists in: {dest}")
        # incase such folder / path exists

# following code to run this backup at a certain date and time, either every day or week or month (preference)
def exec():
    copyFolderTo(source, destination)

schedule.every().day.at("15:40").do(exec)

while True:
    schedule.run_pending() # important as schedule will not run constantly without "run_pending()" function
    time.sleep(60) # the schedule runs every 10 minutes so that it doesn't have to run the whole time
# while loop runs infinitely so that we don't have to run the code manually
