class Coding:

	def python(self):
		print("Python Programming")

class Cloud:

	def aws(self):
		print("AWS Cloud")

class DevOps(Coding, Cloud):

	def tools(self):
		print("Git and Jenkins")


d1 = DevOps()

d1.python()
d1.aws()
d1.tools()
