class Developer:

	def work(self):
		print("Developer is writing python code")

class Tester():

	def work(self):
		print("Tester is Testing the Application")

class Manager():

	def work(self):
		print("Manager is Managing the team")

def process_employee(employee):
	employee.work()

developer = Developer()
tester = Tester()
manager = Manager()

process_employee(developer)
process_employee(tester)
process_employee(manager)	