class company():

	def __init__(self, company_name):
		self.company_name = company_name
		

class Employee(company):
	def __init__(self,company_name, employee_name, salary):
		super().__init__(company_name)

		self.employee_name = employee_name
		self.salary = salary

		
		print("company:", self.company_name)
		print("Employee:", self.employee_name)
		print("Salary:", self.salary)


e1 = Employee("Microsoft", "Jagan", 10000)




    

