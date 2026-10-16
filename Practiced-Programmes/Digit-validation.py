import re

text = "Guru@2026"

result = re.search(r"\d", text)

if result:
	print("Digit Found")

else: 
	print("Digit Not Found")