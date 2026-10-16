class Student:

	college = "Sri Venkateswara Degree College"

	def __init__(self, name, branch):
		self.name = name
		self.branch = branch

	def display(self):
		print("Student Name:", self.name)
		print("Branch:", self.branch)


	@classmethod
	def show_college(cls):
		print("College:", cls.college)


s1 = Student("Jagan", "BCA")
s2 = Student("Hari", "BSC")

s1.display()
s2.display()

Student.show_college()