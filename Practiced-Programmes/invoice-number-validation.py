import re

text = "INV1234A INV12345B INV123456C INV123D INV1234567A"

result = re.findall(r"\bINV\d{4,6}[A-Z]\b", text)

print("Valid Inovice Number:")

print(result)