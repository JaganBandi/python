import re

text = "admin_123 guru2026 admin@123 devops-2026"

result = re.findall(r"\w+", text)

print(result)