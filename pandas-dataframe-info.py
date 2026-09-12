import pandas as pd  

employee_details = {
    "Name": ["Jagan", "Lokesh", "Ram", "Shiva", "Venky", "Kiran"],
    "Department": ["DevOps", "Python", "Testing", "DevOps", "Linux", "Python"],
    "Salary": [35000, 50000, 45000, 65000, 40000, 55000],
    "Experience": [1, 2, 3, 4, 5, 6]
}

employee_df = pd.DataFrame(employee_details)

print(employee_df.info())