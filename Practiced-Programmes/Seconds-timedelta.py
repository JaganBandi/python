from datetime import datetime, timedelta

current_dt = datetime.now()
expiry_time = current_dt + timedelta(seconds=90)

print("OTP Generated Time:", current_dt.strftime("%I:%M:%S %p"))
print("OTP Expire Time:", expiry_time.strftime("%I:%M:%S %p"))
