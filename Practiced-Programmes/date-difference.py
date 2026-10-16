from datetime import datetime

course_started = datetime.strptime("01-07-2026", "%d-%m-%Y")
today_date = datetime.strptime("30-07-2026", "%d-%m-%Y")

difference = today_date - course_started

print("Course Started :", course_started.strftime("%d-%m-%Y"))
print("Today Date :", today_date.strftime("%d-%m-%Y"))
print(difference.days)