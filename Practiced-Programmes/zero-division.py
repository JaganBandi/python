try:
    num1 = int(input("Enter a first number:"))
    num2 = int(input("Enter a second number:"))

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Please Enter a Valid Number")

except ZeroDivisionError:
    print("Cannot Divide By Zero")
