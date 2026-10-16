class employee:

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def display(self):
		print("Employee name:", self.name)
		print("Employee salary:", self.salary)

e1 = employee("Jagan", 50000)
e1.display()