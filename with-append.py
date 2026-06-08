with open("D:/jagan.msg", "a") as file:
	file.write("\n I am learning Python")

with open("D:/jagan.msg", "r") as file:
	data = file.read()
	print(data)

with open("D:/jagan.msg", "w") as file:
	file.write("Remmember Your Goal Jagan\n")

