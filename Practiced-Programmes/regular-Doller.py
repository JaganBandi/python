import re

text = "Welcome to DevOps"

result = re.search("DevOps$", text)

if result:
	print("Pattern is Found")

else: 
	print("Pattern Not Found")