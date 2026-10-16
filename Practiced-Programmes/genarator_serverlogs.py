def read_logs():
	with open("server.log", "r") as file:
		for line in file:
			yield line.strip()

for log in read_logs():
	print("Log:", log)