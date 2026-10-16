from datetime import datetime, timedelta

today = datetime.now()

past_date = today - timedelta(days=30)

print("Today Date:", today.strftime("%d-%m-%Y"))
print("Previous 30 Days Date:", past_date.strftime("%d-%m-%Y"))