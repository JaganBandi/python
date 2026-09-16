import pandas as pd  

employees = {
    "Name": ["Jagan", "Ram", "Kiran", "Shiva", "Venky", "Ravi"],
    "Department": ["Python", "DevOps", "Python", "DevOps", "Python", "DevOps"],
    "Salary": [45000, 60000, 55000, 50000, 70000, 65000]
}

employee_df = pd.DataFrame(employees)

Direction_sorting = employee_df.sort_values(by=["Department", "Salary"], ascending=[True, False])

print(Direction_sorting)