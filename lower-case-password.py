import re

text = "DevOps@2026"

result = re.search(r"[a-z]", text)

if result:
	print("Lowercase Letter Found")

else:
	print("Lowercase Not Found")