class Animal:

	def sound(self):
		print("Animal Sound")


class Dog(Animal):

	def sound(self):
		print("Dog Barking")

d1 = Dog()

d1.sound()