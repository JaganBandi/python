def decorator(function):

	def wrapper(*args):
		print("Before")

		function(*args)

		print("After")

	return wrapper


@decorator
def greet(name, city):
    print(name, "lives in", city)

greet("Jagan", "Anathapur") 
