import os

for item in os.listdir():
	if item.endswith(".py") and os.path.isfile(item):
		print(item)