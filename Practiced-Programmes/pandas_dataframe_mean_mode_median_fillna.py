import pandas as pd  

employees = {
    "Name": ["Jagan", "Ram", "Kiran", "Shiva", "Venky"],
    "Department": ["Python", "DevOps", None, "Python", None],
    "Salary": [45000, 55000, None, 60000, 50000],
    "Experience": [1, 2, 3, None, 5]
}

employee_df = pd.DataFrame(employees)

print("Original Data:", employee_df)

mean_salary = employee_df["Salary"].mean()

employee_df["Salary"] = employee_df["Salary"].fillna(mean_salary)

median_experience = employee_df["Experience"].median()

employee_df["Experience"] = employee_df["Experience"].fillna(median_experience)

mode_department = employee_df["Department"].mode()[0]

employee_df["Department"] = employee_df["Department"].fillna(mode_department)

print("---------- Cleaned Data Frame -------------------")

print("Clean DataFrame:", employee_df)