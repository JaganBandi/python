import shutil

total, used, free = shutil.disk_usage("C:\\")

gb = 1024 ** 3

print("Total Disk :", round(total / gb, 2), "GB")
print("Used Disk  :", round(used / gb, 2), "GB")
print("Free Disk  :", round(free / gb, 2), "GB")

free_precent = (free / total) * 100

print("Free Disk %:", round(free_precent, 2), "%")

if free_precent < 20 :
	print("WARNING : Disk Space Is Low")

else:
	print("Disk Space Is Healthy")