from datetime import datetime

joining_date = datetime.strptime("10-08-2026", "%d-%m-%Y")
today_date = datetime.strptime("30-07-2026", "%d-%m-%Y")

if today_date > joining_date:
	print("Employee is Already Joined")
else:
	print("Employee yet to Join")