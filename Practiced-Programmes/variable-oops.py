class employee:

	company = "Wipro"

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

e1 = employee("Jagan", 30000)

print(e1.name)
print(e1.salary)
print(e1.company)
