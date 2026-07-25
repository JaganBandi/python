import re

text = "I Love Python Programming"

result = re.search("Python", text)

if result:
	print("Pattern Found")

else:
	print("Pattern Not Found")