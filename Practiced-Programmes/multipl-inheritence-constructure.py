class Coding:

	def __init__(self):
		print("Python Coding")

class Cloud:

	def __init__(self):
		super().__init__()
		print("AWS Cloud")

class DevOps(Coding, Cloud):
	def __init__(self):
		super().__init__()
		print("Git and Jenkins")
    
	
d1 = DevOps()
