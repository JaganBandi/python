import pandas as pd  

employee_salaries = pd.Series([30000, 35000, 40000, 45000],
	index=["Jagan", "Harini", "Shiva", "Venky"])

print(employee_salaries)
print(employee_salaries["Shiva"])