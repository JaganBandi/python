class company:

	def __init__(self):
		print("Company: Infosys")

class SoftwareEngineer(company):
	def __init__(self):
		super().__init__()
		print("Role: Software Engineer")


	def work(self):
		print("Devolping Python Application")

e1 = SoftwareEngineer()

e1.work()