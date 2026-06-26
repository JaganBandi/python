class Employee:

	def __init__(self):
		self.__salary = 100000

	def get_salary(self):
		return self.__salary

e1 = Employee()

print("Salary:", e1.get_salary())

