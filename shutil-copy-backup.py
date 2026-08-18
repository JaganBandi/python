import shutil
import os

source = "deployment.txt"
backup_folder = "backup"

if os.path.isfile(source):
	shutil.copy(source, backup_folder)
	print("Backup Created Successfully")