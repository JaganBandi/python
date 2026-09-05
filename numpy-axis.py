import numpy as np  

sales = np.array([
    [10000, 12000, 15000],
    [20000, 22000, 25000],
    [30000, 32000, 35000]
	])

print("Sales:", sales)

monthly_total = np.sum(sales, axis=0)

print("Monthly Sales:", monthly_total)

employee_total = np.sum(sales, axis=1)

print("Employee Total:", employee_total)

average_sales = np.mean(sales, axis=0).astype(dtype=int)

print("Averge Sales:", average_sales)

average_employee = np.mean(sales, axis=1)

print("Average Employee Total:", average_employee)