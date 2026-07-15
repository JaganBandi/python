class InvalidAPIKeyError(Exception):
	pass

class EmptyAPIKeyError(Exception):
	pass

try:
	api_key = input("Enter Your API Key: ")

	if api_key == "":
		raise EmptyAPIKeyError("API Key Cannot Be Empty.")

	if api_key != "DEVOPS123":
		raise InvalidAPIKeyError("Invalid API Key")


except InvalidAPIKeyError as e:
	print(e)

except EmptyAPIKeyError as e:
	print(e)

else:
	print("Connecting to Server...")
	print("Authenticating....")
	print("Fetching Data..")
	print("API Request Successful")
	print("Responce Code: 200k")

finally:
	print("Programme End")
