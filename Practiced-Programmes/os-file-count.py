import os

count = 0

for item in os.listdir():
	if os.path.isdir(item):

		count += 1

print("Total Folders:", count)