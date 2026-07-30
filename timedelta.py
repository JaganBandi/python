from datetime import datetime, timedelta

today = datetime.now()

future_date = today + timedelta(days=15)

print("Today Date:", today.strftime("%d-%m-%Y"))
print("Next Maintenece Date:", future_date.strftime("%d-%m-%Y"))