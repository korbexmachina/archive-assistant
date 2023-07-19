import os
import shutil
import datetime

# Paths and list of files
vaultPath = "./notes" # PATH TO VAULT
backupPath = "./vault-backup" # PATH TO BACKUP DIRECTORY

if not os.path.exists(vaultPath):
    os.mkdir(vaultPath)

if not os.path.exists(backupPath):
    os.mkdir(backupPath)

daily = 0
monthly = 0

date = datetime.date.today()

for i in os.listdir(backupPath):
    # print(i)
    if i.__contains__("daily-backup"):
        daily += 1
    if i.__contains__("monthly-backup"):
        monthly += 1

if daily >= 30: # Check if it is time to create a monthly backup
    shutil.make_archive(f"monthly-backup-{date}", "gztar", vaultPath)
    try:
        shutil.move(f"./monthly-backup-{date}.tar.gz", backupPath)
    except:
        os.remove(f"./monthly-backup-{date}.tar.gz")
        print("Already created a backup for today, try again tomorrow!")

    # Delete the now outdated archives
    for i in  os.listdir(backupPath):
        if i.__contains__("monthly-backup"):
            death = os.path.join(backupPath, i)
            os.remove(death)

elif monthly >= 12: # Check if it is time to create an annual backup
    shutil.make_archive(f"annual-backup-{date}", "gztar", vaultPath)
    try:
        shutil.move(f"./annual-backup-{date}.tar.gz", backupPath)
    except:
        os.remove(f"./annual-backup-{date}.tar.gz")
        print("Already created a backup for today, try again tomorrow!")

    for i in os.listdir(backupPath):
        if i.__contains__("monthly-backup"):
            death = os.path.join(backupPath, i)
            os.remove(death)

else: # Otherwise create a daily backup
    shutil.make_archive(f"daily-backup-{date}", "gztar", vaultPath)
    try:
        shutil.move(f"./daily-backup-{date}.tar.gz", backupPath)
    except:
        os.remove(f"./daily-backup-{date}.tar.gz")
        print("Already created a backup for today, try again tomorrow!")

