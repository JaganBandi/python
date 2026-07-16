class InvalidUsernameError(Exception):
	pass

class InvalidPasswordError(Exception):
	pass

try:

	username = input("Enter Your username: ")
	password = input("Enter Your Password: ")

	if username != "admin":
		raise InvalidUsernameError("Inavlid Username")

	if password != "admin@123":
		raise InvalidPasswordError("Inavlid Password")

except InvalidUsernameError as e: 
	print(e)

except InvalidPasswordError as e:
	print(e)

else:
	print("Login SuccessFully")

finally:
	print("Thank You For Using System")
	print("Programme End")