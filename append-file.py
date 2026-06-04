file = open("D:/jagan.msg", "r")

data = file.read()

file.close()

file = open("D:/jagan.msg", "a")

file.write("\nGood to See you Jagan")

print(data)

file.close()
