import numpy as np   

sales = np.array([1000, 2000, 3000, 4000])

sales_copy = sales.copy()

sales_copy[2] = 5000
sales_copy[3] = 6000

print("Original Sales:", sales)
print("Sales Copy :", sales_copy)