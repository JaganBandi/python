import shutil
import os

source = "Employee-Salary-System"
destination = "backup_folder"

if os.path.isdir(source):
	shutil.copytree(source, destination, dirs_exist_ok=True)
	print("Backup Folder Created Successfully")

else:
	print("Error: The Source Folder Is Not Found")
