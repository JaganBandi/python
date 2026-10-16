def votting(age):

	if age >= 18:
		print("You Are Eligible For Vote")

	else: 
		print("Not Eligible")

age = int(input("Enter your age:"))

votting(age)