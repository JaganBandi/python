fiber_names = ["Jio", "Aitel", "Bsnl", "Idea", "Vadaphone"]

fiber_iterator = iter(fiber_names)

while True:
	try :
		fiber = next(fiber_iterator)
		print("Fiber Names:", fiber)
		print("----------------------------")

	except StopIteration:
		break