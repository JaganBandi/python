import os

for item in os.listdir():
	if item.startswith("o") and os.path.isfile(item):
		print(item)