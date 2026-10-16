class student:

	def __init__(self, name, m1, m2, m3):
		self.name = name
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def display(self):
		print("Student Name:", self.name)

	def total(self):
		total = self.m1 + self.m2 + self.m3
		print("Total:", total)

	def average(self):
		average = (self.m1 + self.m2 + self.m3) / 3
		print("Average:", average)

s1 = student("Jagan", 80, 90, 70)

s1.display()
s1.total()
s1.average()
