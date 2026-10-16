import re

text = "STU101 STU9999 STU12 STU12345"

result = re.findall(r"\bSTU\d{3,4}\b", text)

print("Valid Student Roll Number")

for code in result:
	print(code)
