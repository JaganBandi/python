file = open("company.txt", "w")
file.write("Infosys\n")
file.write("Wipro\n")
file.write("TCS")

file.close()

file = open("company.txt", "r")
data = file.read()

print(data)

file.close()

file = open("company.txt", "a")

file.write("\nHCL")

file.close()