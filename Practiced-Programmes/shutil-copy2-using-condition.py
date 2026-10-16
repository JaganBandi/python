import shutil
import os

source = "deployment.txt"
backup = "backup_folder/deployment.txt"

if os.path.isfile(source):
	shutil.copy2(source, backup)
	print("Deployment Backup Created Successfully")

else:
	print("ERROR: deployment.txt file not found")