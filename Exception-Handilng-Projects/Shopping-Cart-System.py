class OutOfStock(Exception):
	pass

class InvalidQuantityError(Exception):
	pass

try:
	product = "Laptop"
	price = 50000
	stock = 5

	print("-----Shopping Cart---------")
	print("Product :", product)
	print("Price:", price)
	print("Stock:", stock)

	quantity = int(input("Enter Your Quantity: "))

	if quantity <= 0:
		raise InvalidQuantityError("Quantity Must Be Greater Than Zero")

	if quantity > stock:
		raise OutOfStock("Requested Quantity is Not Avaliable")

except InvalidQuantityError as e:
	print(e)

except OutOfStock as e:
	print(e)

else:
	Total = quantity * price
	print("\n Order Placed Successfully")
	print("Total Amount:", Total)
	print("Thank You For Shopping!")

finally:
	print("Programe End")