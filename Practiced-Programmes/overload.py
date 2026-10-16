class ShoppingCart:

	def __init__(self, total):
		self.total = total

	def __add__(self, other):
		return self.total + other.total


cart1 = ShoppingCart(2500)
cart2 = ShoppingCart(5500)


total = cart1 + cart2

print("Combined cart total:", total)