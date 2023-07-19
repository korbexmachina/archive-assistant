#!/usr/bin/env python

import os
import sys
import shutil
import datetime
import time

def move(type, date, archivePath) -> None:
    try:
        shutil.move(f"./{type}-{date}.tar.gz", archivePath)
        print(f"Archive created! {type}-{date}.tar.gz")
    except:
        os.remove(f"./{type}-{date}.tar.gz")
        print(f"Already created a backup for today, try again tomorrow! {type}-{date}.tar.gz")
    return

def cleanup(type, archivePath) -> None:
    # Delete the now outdated archives
    for i in  os.listdir(archivePath):
        if i.__contains__(type):
            death = os.path.join(archivePath, i)
            os.remove(death)

def main():

    CONST_PATH = os.path.expanduser("~/.config/autoArchive/archivePaths.txt") # The path to the config file that contains the paths

    if not os.path.exists(CONST_PATH):
        os.mkdir(CONST_PATH)

    # Paths
    with open(os.path.expanduser('~/.config/autoArchive/archivePaths.txt'),'r') as sys.stdin:
        vaultPath = os.path.expanduser(input()) # PATH TO VAULT
        archivePath = os.path.expanduser(input()) # PATH TO BACKUP DIRECTORY

    if not os.path.exists(vaultPath):
        os.mkdir(vaultPath)

    if not os.path.exists(archivePath):
        os.mkdir(archivePath)

    daily = 0
    monthly = 0
    clean = ""
    date = datetime.date.today()

    for i in os.listdir(archivePath):
        # print(i)
        if i.__contains__("daily-archive"):
            daily += 1
        elif i.__contains__("monthly-archive"):
            monthly += 1

    if daily >= 30: # Check if it is time to create a monthly backup
        type = "monthly-archive"
        clean = "daily archive"
    elif monthly >= 12: # Check if it is time to create an annual backup
        type = "annual-archive"
        clean = "monthly-archive"
    else: # Otherwise create a daily backup
        type = "daily-archive"

    shutil.make_archive(f"{type}-{date}", "gztar", vaultPath)
    move(type, date, archivePath)

    if clean != "":
        cleanup(clean, archivePath)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Executed at: {datetime.datetime.now()} in {(end - start):.2f} seconds\n") # Timestamp for debbuging
