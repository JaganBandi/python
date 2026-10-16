import re

logs = """
2026-07-27 09:15:12 INFO  Server started successfully
2026-07-27 09:15:18 INFO  Database connection established
2026-07-27 09:16:01 ERROR Database connection failed
2026-07-27 09:16:15 WARNING Disk space is low
2026-07-27 09:17:03 ERROR User authentication failed
2026-07-27 09:18:20 INFO  Backup completed successfully
2026-07-27 09:19:55 ERROR File not found
2026-07-27 09:20:30 WARNING High CPU usage detected
"""

result = re.findall("ERROR.*", logs)

for log in result:
    print(log)