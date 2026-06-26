class Payment:

	def pay(self):
		print("Processing Payment")

class UPI(Payment):

	def pay(self):
		print("Processing UPI Payment")

class CreditCard(Payment):

	def pay(self):
		print("Processing Credit Card Payment")

class NetBanking(Payment):
	def pay(self):
		print("Processing NetBanking Payment")

u1 = UPI()
c1 = CreditCard()
n1 = NetBanking()

u1.pay()
c1.pay()
n1.pay()


