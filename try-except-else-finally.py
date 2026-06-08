try:
	num1 = int(input("Enter a first number:"))
	num2 = int(input("Enter a Second number:"))
	num = num1 + num2

except ValueError:
	print("Invalid Error")

else:
	print("you enteres:", num)

finally:
	print("Programme Ended")
