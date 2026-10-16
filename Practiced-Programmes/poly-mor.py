class Employee:

	def work(self):
		print("Employee is Working")

class Developer(Employee):

	def work(self):
		print("Devoloper is writing python code")

class Tester(Employee):

	def work(self):
		print("Tester is testing the application")


employee = Employee()
developer = Developer()
tester = Tester()

employee.work()
developer.work()
tester.work()
