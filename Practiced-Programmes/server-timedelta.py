from datetime import datetime, timedelta

current_time = datetime.now()

server_time = current_time + timedelta(hours=2)

print("Current Time:", current_time.strftime("%H"))
print("Server Restart Time:", server_time.strftime("%H"))
