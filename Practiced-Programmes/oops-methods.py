from abc import ABC, abstractmethod

class Employee(ABC):

	def __init__(self, name, salary):
		self.name = name
		self.__salary = salary

	def get_salary(self):
		return self.__salary

	def set_salary(self,salary):

		if salary >= 30000:
			self.__salary = salary

		else:
			print("Salary Must be Atleast 30000")


	@abstractmethod
	def work(self):
		pass

class Developer(Employee):

	def work(self):
		print(self.name, "is writing Python code")

class Tester(Employee):

	def work(self):
		print(self.name, "is testing the application")



def process_employee(employee):
	employee.work()

developer = Developer("Jagan", 50000)
tester = Tester("Kalyan", 45000)

process_employee(developer)
process_employee(tester)

print(developer.get_salary())
developer.set_salary(70000)
print(developer.get_salary())
developer.set_salary(20000)
print(developer.get_salary())


