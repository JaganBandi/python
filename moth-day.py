from datetime import datetime

taday_attendence = datetime.now()

print("Day Name: ", taday_attendence.strftime("%A"))
print("Short Day Name: ", taday_attendence.strftime("%a"))
print("Month Name: ", taday_attendence.strftime("%B"))
print("Short Month Name: ", taday_attendence.strftime("%b"))