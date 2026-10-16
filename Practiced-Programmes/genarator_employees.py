def employee_data():
	employees = ["Jagan", "Maneesha", "Hymavathi", "Lokesh", "Mahesh"]

	for employee in employees:
		yield employee

employees = employee_data()

for employee in employees:
     print("Processing:", employee)