import json

employee = {
	"name": "Maneesha",
	"department": "HR Management",
	"id": 103

}

file = open("employee.json", "w")

json.dump(employee, file)

print(employee)

file.close()

print("Data Stored Successfully")