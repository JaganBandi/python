import pandas as pd   

employees = {
    "Name": ["Jagan", "Ram", "Kiran", "Shiva", "Venky"],
    "Department": ["Python", None, "DevOps", "Python", None],
    "Salary": [45000, 55000, None, 60000, 50000],
    "Experience": [1, 2, 3, None, 5]
}


employee_df = pd.DataFrame(employees)

print("Original Data:", employee_df)

Missing_Values = pd.isna(employee_df)

print(Missing_Values)

Missing_method2 = pd.isnull(employee_df)

print(Missing_method2)

print(employee_df.isna().sum())