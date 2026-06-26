class Employee:

	def __init__(self):
		self.__salary = 100000

	def get_salary(self):
		return self.__salary

	def set_salary(self, salary):
		self.__salary = salary


e1 = Employee()

e1.set_salary(150000)

print("Salary:", e1.get_salary())
