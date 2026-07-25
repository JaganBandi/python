import re

text = "PRD12345 PRD1234 PRD56789 ABC12345 PRD99999"

result = re.findall(r"\bPRD\d{5}\b", text)

print(result)