class student:

	college = "Sri venkateswara College"


	@classmethod
	def show_college(cls):
		print("College:", cls.college)

student.show_college()