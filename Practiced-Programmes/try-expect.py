try:
    num1 = int(input("Enter a first number:"))
    num2 = int(input("Enter a second number:"))

    result = num1 + num2

    print("result:", result)

except ValueError:
    print("Please Enter Valid Number")

