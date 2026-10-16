import re

password = "Jagan@2026"

length = re.fullmatch(r".{8,}", password)

uppercase = re.search(r"[A-Z]", password)

lowercase = re.search(r"[a-z]", password)

digit = re.search(r"\d", password)

specialCharacter = re.search(r"[@#$%&*!]", password)

if length and uppercase and lowercase and digit and specialCharacter:

	print("Vaild Password")

else:
	print("Invalid Password")