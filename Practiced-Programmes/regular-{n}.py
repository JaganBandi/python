import re

text = "EMP1234A EMP5678B EMP123C EMP9999Z EMP12345A"

result = re.findall(r"\bEMP\w{4}[A-Z]\b", text)

print(result)