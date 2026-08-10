import os

os.chdir("D:\\linux-commands")

file = open("Jagan.txt", "w")

file.write("Hello this is testing file using os.chdir method the os methods")

file.close()

print(os.getcwd())