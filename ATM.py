balence = 30000

print("=======ATM======")
print("1.Check Balene")
print("2.Deposit")
print("3.Withdraw")
print("4.Exit")

choice = int(input("Enter your Choice:"))

if choice == 1:
	print("Current Balence:", balence)

elif choice == 2:
	amount = int(input("Enter Your deposit amount:"))

	balence = balence + amount

	print("Balence:", balence)

elif choice == 3:
    amount = int(input("Enter Your Withdraw amount:"))

    if amount > balence:
        print("Insufficiant balence")

    else:
        balence = balence - amount

        print("Balence:", balence)

elif choice == 4:
	print("Thank you")

else:
	print("Invalid")