from datetime import datetime, timedelta

exam_date = datetime.strptime("30-07-2026", "%d-%m-%Y")
new_exam_date = exam_date + timedelta(days=20)

print("Exam Date:", exam_date.strftime("%d-%m-%Y"))
print("New Exam Date:", new_exam_date.strftime("%d-%m-%Y"))