class Employee:

	def __init__(self):
		self.__salary = 50000


	def show_salary(self):

		print("Salary:", self.__salary)

e1 = Employee()
e1.show_salary()