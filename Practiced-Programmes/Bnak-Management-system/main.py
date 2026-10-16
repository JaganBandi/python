import bank

intial_balence = int(input("Enter your intial balence:"))
deposite = int(input("Enter your Deposite ammount:"))
withdraw = int(input("Enter yout withdraw ammount:"))

balence = bank.deposite(intial_balence, deposite)
print("After Deposite:", balence)

if withdraw > balence:
	print("insufficiant Balence")

else:
	balence = bank.withdraw(balence, withdraw)
	print("Final Balence:", balence)

