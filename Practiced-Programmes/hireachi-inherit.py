class Employee:

	def __init__(self, name):
		self.name = name

	def dispaly_name(self):
		print("Employee Name:", self.name)

class Developer(Employee):

	def write_code(self):
		print("Developer Write Code")

class Tester(Employee):

	def test_application(self):
		print("Tester is Tesing the Application")

developer = Developer("Jagan")
developer.dispaly_name()
developer.write_code()

tester = Tester("Kalyan")
tester.dispaly_name()
tester.test_application()