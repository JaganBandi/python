class Developer:

	def write(self):
		print("Developer is Writing Code")

class Tester:
	
	def test_code(self):
		print("Tester is testing code")

class DevOpsEngineer(Developer, Tester):

	def deploy(self):
		print("DevOps Engineer is Deploying Application")

devopsengineer = DevOpsEngineer()

devopsengineer.write()
devopsengineer.test_code()
devopsengineer.deploy()
 