def car():
	print("Car Started")

def engine(func):

	def start():
		print("Engine Started")
		func()

	return start


car = engine(car)

car()