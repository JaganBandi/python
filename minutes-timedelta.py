from datetime import datetime, timedelta

current_time = datetime.now()
backup = current_time + timedelta(minutes=45)

print("Current Time:", current_time.strftime("%H:%M:%S %p"))
print("Datebase Backup Time:", backup.strftime("%I:%M:%S %p"))
