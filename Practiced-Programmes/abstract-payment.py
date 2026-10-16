from abc import ABC , abstractmethod

class Payment(ABC):

	@abstractmethod
	def pay(self, amount):
		pass

class UPIPayment(Payment):

	def pay(self, amount):
		print("Paid",amount, "using UPI")

class CardPayment(Payment):

	def pay(self, amount):
		print("Paid", amount, "Using credit Card")

upi = UPIPayment()
card = CardPayment()

upi.pay(500)
card.pay(1000)

