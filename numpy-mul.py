import numpy as np  

salaries = np.array([30000, 40000, 50000, 60000])

print("Original salaries:", salaries)

increment = (salaries * 1.10).astype(int)

print("Increment Salaries:", increment)

print(increment.dtype)