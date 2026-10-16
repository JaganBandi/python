file = open("employee.txt", "w")
file.write("Infosys")
file.close()

file = open("employee.txt", "r")
data = file.read()

print(data)

file.close()
