def employee(**details):

	for key, value in details.items():
		print(key, ":", value)

employee(name="JAGAN", Department="DevOps", company="Infosys", salary=50000)
