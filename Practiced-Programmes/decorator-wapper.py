def connect_database(func):

	def wrapper():
		print("Connecting Database...")
		func()

	return wrapper

@connect_database
def employee_records():
	print("Fetching Employee Records...")

employee_records()