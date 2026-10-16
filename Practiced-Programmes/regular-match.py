import re 

text = "Jenkins is a one of the tool in DevOps"

result = re.match("tool", text)

print(result)