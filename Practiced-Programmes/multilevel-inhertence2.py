class Organozation:

	def company_info(self):
		print("Comapny: Google")

class Department(Organozation):
	def department_name(self):
		print("Department: IT")


class Employee(Department):
	def employee_name(self):
		print("Employee Name: Jagan")

e1 = Employee()

e1.company_info()
e1.department_name()
e1.employee_name()
