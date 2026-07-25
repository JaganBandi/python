import re

text = "color, colour"

result = re.findall(r"colou?r", text)

print(result)