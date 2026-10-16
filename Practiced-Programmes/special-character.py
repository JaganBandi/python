import re

text = "Guru@2026"

result = re.search(r"[%@!*#$&]", text)

if result:
	print("Special Character Found")

else:
	print("Special Character Not Found")