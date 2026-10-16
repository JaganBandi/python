class BankAccount:

	def __init__(self):
		self.__balance = 10000


	def get_balance(self):
		return self.__balance

	def deposit(self, amount):
		self.__balance += amount

b1 = BankAccount()

print("Before Deposit:", b1.get_balance())

b1.deposit(5000)

print("After Deposit:", b1.get_balance())