def check_salary_access(function):

	def wrapper(*args, **kwargs):

		if args:
			salary = args[1]

		else:
			salary = kwargs["salary"]

		if salary >= 50000:
			function(*args, **kwargs)

		else:
			print("Access Denied: Salary is below the required level")

	return wrapper

@check_salary_access
def salary_details(employee, salary):
	print("Employee:", employee, "Salary:", salary)

salary_details("Jagan", 60000)
salary_details("Ram", 40000)

salary_details(employee="Shiva", salary=70000)
salary_details(employee="Ravi", salary=40000)
