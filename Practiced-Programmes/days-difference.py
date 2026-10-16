from datetime import datetime

today_date = datetime.strptime("30-07-2026", "%d-%m-%Y")
interview_date = datetime.strptime("15-08-2026", "%d-%m-%Y")

difference = interview_date - today_date

print("Today Date : ", today_date.strftime("%d-%m-%Y"))
print("Interview Date : ", interview_date.strftime("%d-%m-%Y"))
print(difference.days)
