import re

logs = "ERROR, ERRORR, ERRORRRR, ERRORRRRR"

result = re.findall("ERRORR*", logs)

print(result)