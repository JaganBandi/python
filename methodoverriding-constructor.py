class Vehical:

	def start(self):
		print("Vehical Started")

class Car(Vehical):

	def start(self):
		super().start()
		print("Car Started")

c1 = Car()

c1.start()