employees = ["Jagan", "Ravi", "Srinu", "Ram", "Arun"]

employee_iterator = iter(employees)

while True:
	try:
		employee = next(employee_iterator)
		print("Processing Employees:", employee)

	except StopIteration:
		break