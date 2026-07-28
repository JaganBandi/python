import re

text = """

jagan12@gmail.com
kalyan@gmail.com
devops.2026@gmail.com
python.devoloper@gmail.com
guru@gmail
guru@.com
"""
result = re.findall(r"\b[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", text)

print(result)
