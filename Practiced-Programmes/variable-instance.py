class employee:

	company = "Wipro"

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def display(self):
		print("Employee Name:", self.name)
		print("Salary:", self.salary)
		print("Company:", employee.company)

e1 = employee("Shiva", 60000)

e1.display()
