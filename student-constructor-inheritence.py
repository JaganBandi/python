class student:

	def __init__(self):
		print("Student Constructor")


class EngineeringStudent(student):


	def __init__(self):

		super().__init__()

		print("Engineering Student Constructor")

s1 = EngineeringStudent()