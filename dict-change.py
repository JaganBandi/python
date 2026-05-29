employee = {"Name": "Jagan", "Department": "Development", "Age": 21, "salary": 50000}

print(employee)

employee ["Department"] = "Devops"

print(employee)

x = employee.keys()
print(x)

employee.update({"Age": 23})
print(employee)

y = employee.items()
print(y)

z = employee.values()

employee ["salary"] = 80000
print(z)

a = employee.get("Name")

print(a)

employee ["location"] = "Hydrabad"
print(employee)

employee.update({"company": "Infosys"})
print(employee)

employee.pop("location")
print(employee)

employee.popitem()
print(employee)

employee.clear()
print(employee)


