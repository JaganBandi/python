import re

password = "devops@123"

result = re.fullmatch(r".{8,}", password)

print(result)