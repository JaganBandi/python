class Employee:

	def __init__(self, name, salary):
		self.name = name
		self.__salary = salary

	def get_salary(self):
		return self.__salary

	def set_salary(self, salary):

		if salary >=30000:
			self.__salary = salary
			print("Salary Updated")

		if salary < 30000:
			print("Salary Must be at least 30000")

employee = Employee("Jagan", 50000)

print(employee.get_salary())

employee.set_salary(60000)

print(employee.get_salary())

employee.set_salary(20000)

print(employee.get_salary())

