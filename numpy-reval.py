import numpy as np 

sales = np.array([
	[10000, 12000, 15000],
    [20000, 22000, 25000],
    [30000, 32000, 35000]
    ])

flat_sales = sales.ravel()

print(flat_sales)
print(flat_sales.shape)
print(flat_sales.ndim)
print(flat_sales.dtype)
print(flat_sales.reshape(-1, 3))