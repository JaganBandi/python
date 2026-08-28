import numpy as np  

sales = np.array([
	[50000, 55000, 60000],
	[30000, 35000, 40000],
	[20000, 22000, 25000],
	[15000, 18000, 20000]
	])

print("Sales Data  :", sales)
print("Shape       :", sales.shape)
print("Dimensions  :", sales.ndim)
print("Total Values:", sales.size)
print("Data Type   :", sales.dtype)
