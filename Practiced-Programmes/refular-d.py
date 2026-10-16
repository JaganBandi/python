import re 

text = "1234 123 12345 5678 9999"

result = re.findall(r"\d{4}", text)

print(result)