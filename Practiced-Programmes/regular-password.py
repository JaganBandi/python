import re

passwords = [

"Guru@2026"
"devops@2026"
]

for password in passwords:

    result = re.search(r"[A-Z]", password)

    if result:
	    print(password,"->Uppercase Found")
    else: 
	    print(password, "->Uppercase Not Found")