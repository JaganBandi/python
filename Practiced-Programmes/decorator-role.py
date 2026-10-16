def check_role(function):

	def wrapper(*args, **kwargs):

		if args[1] == "admin":
			function(*args, **kwargs)

		else:
			print("Access Denied: Admin Only")

	return wrapper

@check_role
def admin_page(username, role):
	print("Username:", username , "Role", role)

admin_page("Jagan", "admin")
admin_page("Ram", "user")