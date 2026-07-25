import re

text = "Welcome to DevOps"

result = re.search("DevOps$", text)

if result:
	print("Ends with DevOps")

else:
	print("Deosn't ends with DevOps")