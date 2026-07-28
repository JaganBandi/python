import re

text = "Python123"

result = re.fullmatch(r"\w+", text)

print(result)