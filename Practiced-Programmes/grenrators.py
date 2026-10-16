def employee_name():
	yield "Jagan"
	yield "Ram"
	yield "Shiva"
	yield "Kiran"

employees = employee_name()

print(next(employees))
print(next(employees))
print(next(employees))
print(next(employees))