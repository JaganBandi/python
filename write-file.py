file = open("D:/jagan.msg", "w")

file.write("witten by jagan\n")

file.write("this is mine")

file.close()

file = open("D:/jagan.msg", "r")

data = file.read()

print(data)

file.close()
