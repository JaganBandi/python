class Employee:

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def display_employee(self):
		print("Employee:", self.name)
		print("Salary  :", self.salary)

class Manager(Employee):

	def __init__(self, name, salary, team_size):
		super().__init__(name, salary)
		self.team_size = team_size

	def display_manager(self):
		print("Employee Name:", self.name)
		print("Salary       :", self.salary)
		print("Team Size    :", self.team_size)


manager = Manager("Jagan", 60000, 5)

manager.display_manager()