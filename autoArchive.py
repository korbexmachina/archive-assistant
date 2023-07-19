#!/usr/bin/env python

import os
import shutil
import datetime

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
    # Paths and list of files
    vaultPath = os.path.expanduser("~/notes") # PATH TO VAULT
    archivePath = os.path.expanduser("~/vault-archive") # PATH TO BACKUP DIRECTORY

    if not os.path.exists(vaultPath):
        os.mkdir(vaultPath)

    if not os.path.exists(archivePath):
        os.mkdir(archivePath)

    daily = 0
    monthly = 0

    date = datetime.date.today()

    for i in os.listdir(archivePath):
        # print(i)
        if i.__contains__("daily-backup"):
            daily += 1
        elif i.__contains__("monthly-backup"):
            monthly += 1

    if daily >= 30: # Check if it is time to create a monthly backup
        type = "monthly-archive"
        shutil.make_archive(f"{type}-{date}", "gztar", vaultPath)
        move(type, date, archivePath)
        cleanup(type, archivePath)

    elif monthly >= 12: # Check if it is time to create an annual backup
        type = "annual-archive"
        shutil.make_archive(f"{type}-{date}", "gztar", vaultPath)
        move(type, date, archivePath)
        cleanup(type, archivePath)

    else: # Otherwise create a daily backup
        type = "daily-archive"
        shutil.make_archive(f"{type}-{date}", "gztar", vaultPath)
        move(type, date, archivePath)

if __name__ == "__main__":
    main()
