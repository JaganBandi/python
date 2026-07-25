import re

text = "Employee id = 123456780"

result = re.findall("\d", text)

print(result)