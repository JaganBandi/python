import pandas as pd  

employees = {
    "Name": ["Jagan", "Ram", "Kiran", "Shiva", "Venky"],
    "Department": ["Python", None, "DevOps", "Python", None],
    "Salary": [45000, 55000, None, 60000, 50000],
    "Experience": [1, None, 3, 4, 5]
}

employee_df = pd.DataFrame(employees)

print("Original Data:", employee_df)

print(employee_df.isna())

Clean_df = employee_df.fillna(0)

print("Fill Data:", Clean_df)

print("------------Specific Columns-------------")

employee_df["Department"] = employee_df["Department"].fillna("Unknown")

employee_df[["Experience", "Salary"]] = employee_df[["Experience", "Salary"]].fillna(0)

print(employee_df)
