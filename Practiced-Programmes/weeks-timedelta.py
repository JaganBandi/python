from datetime import datetime, timedelta

today = datetime.now()

future_weeks = today + timedelta(weeks=4)

print("Today Date:", today.strftime("%d-%m-%Y"))
print("Next Security Audit:", future_weeks.strftime("%d-%m-%Y"))