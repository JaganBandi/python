users = [

{"id": 1, "name": "Jagan"},
{"id": 2, "name": "Kiran"},
{"id": 3, "name": "Raju"}

]

user_iterator = iter(users)

while True:

	try:
		user = next(user_iterator)
		print("User ID:", user["id"])
		print("User Name:", user["name"])
		print("-------------------------")

	except StopIteration:
		break
