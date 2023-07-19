import os
import shutil
import datetime

path = os.getcwd()
if not os.path.exists(path + "./vault-backup"):
    os.mkdir(path + "./vault-backup")

# Paths and list of files
vaultPath = "~/notes"
backupPath = "./vault-backup"

daily = 0
monthly = 0

for i in  os.listdir(backupPath):
    # print(i)
    if i.__contains__("daily-backup"):
        daily += 1
    if i.__contains__("monthly-backup"):
        monthly += 1

if daily >= 30:
    shutil.make_archive(f"daily-backup {datetime.date.today()}", 'tgz', vaultPath)
    for i in  os.listdir(backupPath):
        death = os.path.join(backupPath, i)
        os.remove(death)
if monthly >= 12:
    shutil.make_archive(f"monthly-backup-{datetime.date.today()}", 'tgz', vaultPath)
