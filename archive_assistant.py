#!/usr/bin/env python

import os
import sys
import shutil
import datetime
import time

def move(type, date, archive_path) -> None:
    try:
        shutil.move(f"./{type}-{date}.tar.gz", archive_path)
        print(f"Archive created! {type}-{date}.tar.gz")
    except:
        os.remove(f"./{type}-{date}.tar.gz")
        print(f"Already created an archive for today, try again tomorrow!\n{type}-{date}.tar.gz")
    return

def cleanup(type, archive_path) -> None:
    # Delete the now outdated archives
    for i in  os.listdir(archive_path):
        if i.__contains__(type):
            death = os.path.join(archive_path, i)
            os.remove(death)

def main():

    CONST_PATH = os.path.expanduser("~/.config/autoArchive/archivePaths.txt") # The path to the config file that contains the paths

    if not os.path.exists(CONST_PATH):
        os.mkdir(CONST_PATH)

    # Paths
    with open(os.path.expanduser('~/.config/autoArchive/archivePaths.txt'),'r') as sys.stdin:
        vault_path = os.path.expanduser(input()) # PATH TO VAULT
        archive_path = os.path.expanduser(input()) # PATH TO BACKUP DIRECTORY

    if not os.path.exists(vault_path):
        os.mkdir(vault_path)

    if not os.path.exists(archive_path):
        os.mkdir(archive_path)

    daily = 0
    monthly = 0
    clean = ""
    date = datetime.date.today()

    for i in os.listdir(archive_path):
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

    shutil.make_archive(f"{type}-{date}", "gztar", vault_path)
    move(type, date, archive_path)

    if clean != "":
        cleanup(clean, archive_path)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    # Timestamp for debbuging
    current_time = datetime.datetime.now()
    print(f"Executed at: {current_time.time()} in [[ {(end - start):.2f} ]] seconds\n")
