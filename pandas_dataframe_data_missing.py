import pandas as pd  

employees = {
    "Name": ["Jagan", "Ram", "Kiran", "Shiva"],
    "Department": ["Python", None, "DevOps", "Python"],
    "Salary": [45000, 55000, None, 60000]
}


employee_df = pd.DataFrame(employees)

print("Original DataFrame :", employee_df)

print(employee_df.isna())

print(employee_df.isnull().sum())

Cleaned_df = employee_df.dropna()

print(Cleaned_df)