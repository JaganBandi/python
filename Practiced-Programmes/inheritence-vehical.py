class vehical:

	def __init__(self, name):
		self.name = name
	
	def start(self):
		print("Vehical Name :", self.name)
		print(self.name,"has started")

class Car(vehical):

	def drive(self): 
		print(self.name," is Driving")

car = Car("Toyota")

car.start()
car.drive()
