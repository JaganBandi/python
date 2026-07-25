import re

text = "cat bat rat mat hat"

result = re.findall("[br]at", text)

print(result)