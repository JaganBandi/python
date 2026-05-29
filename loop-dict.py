tools = {
   "pipeline": "jenkins",
   "container": "docker",
   "Quality": "SonarQube",
   "webapplication": "Tomcat"
}

for key in tools.keys():
   print(key)

for value in tools.values():
  print(value)
       
for x, y in tools.items():
  print(x, y)

