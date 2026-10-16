class Person:

	def __init__(self, name):
		self.name = name
	
	def display_method(self):
		print("Person Name:", self.name)

class Employee(Person):

	def work(self):
		print("Employee Working in a Company")

class Manager(Employee):

	def manage_team(self):
		print("Manager is managing the company")



manager = Manager("Jagan")

manager.display_method()
manager.work()
manager.manage_team()
print(Manager.mro())