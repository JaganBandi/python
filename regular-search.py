import re

text = "DevOps is Awesome"

result = re.search("^DevOps", text)

if result:
	print("Start With DevOps")

else: 
	print("Does Not Start With DevOps")