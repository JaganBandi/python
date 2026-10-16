class University:

	def University_name(self):
		print("Andhra University")

class Teacher(University):
	def teacher_studies(self):
		print("Completed B.E.D")

class Professor(Teacher):
	def professor_studies(self):
		print("Completed P.hd")

p1 = Professor()

p1.University_name()
p1.teacher_studies()
p1.professor_studies()