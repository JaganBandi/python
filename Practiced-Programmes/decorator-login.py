def login_required(function):

	def wrapper(username, logged_in):
		if logged_in:
			function(username)
			
		else:
			print("Access Denied! please login")


	return wrapper

@login_required
def dashboard(username):
	print("Welcome to dashboard:", username)

dashboard("Jagan", True)
dashboard("Kiran", False)
			



