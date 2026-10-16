class BankAccount:

	def __init__(self, account_holder, balence):
		self.account_holder = account_holder
		self.__balence = balence

	@property
	def balence(self):
		return self.__balence

	@balence.setter
	def balence(self, balence):
		if balence > 0:
			self.__balence = balence

		else:
			print("Balence Cannot be negitive")

account = BankAccount("Jagan", 10000)
print(account.balence)

account.balence = 15000
print(account.balence)

account.balence = -1500
print(account.balence)
