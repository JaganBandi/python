import os

count = 0

for item in os.listdir():
	if os.path.isfile(item):
		
		count += 1

print("Total Files :", count)