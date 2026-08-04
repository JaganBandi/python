import json

file = open("employee.json", "r")

employee = json.load(file)

print(employee)

file.close()