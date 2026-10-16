from datetime import datetime

attendence = datetime.now()

print("=" *55)
print("      Employee Attendence Report")
print("=" *55)
print("Date:", attendence.strftime("%d-%m-%Y"))
print("Day:", attendence.strftime("%A"))
print("Month:", attendence.strftime("%B"))
print("Login Time:", attendence.strftime("%I:%M:%S %p"))
print("=" *55)