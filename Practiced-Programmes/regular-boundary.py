import re

text = "EMP1234 EMP5678 EMP123 EMP12345 ABC1234 EMP9999"

result = re.findall(r"\bEMP\d{4}\b", text)

print(result)