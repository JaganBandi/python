def api_logger(func):

	def wrapper(*args, **kwargs):
		print("Logging API Request.....")
		func(*args, **kwargs)

	return wrapper

@api_logger

def get_user(username):
	print("Fetching user details for:", username)

get_user(username="jagan")