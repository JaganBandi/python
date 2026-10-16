def employee_salaries():
	employees = [
	     ("Jagan", 30000),
	     ("Ram", 40000),
	     ("Shiva", 60000),
	     ("Maneesha", 45000)
	     ]

	for employee in employees:
		yield employee

employees = employee_salaries()

for employee, salary in employees:
	print("Employee :",employee , "Salary:", salary )