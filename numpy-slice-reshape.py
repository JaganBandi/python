import numpy as np 

sales = np.array([
	5000, 6000, 7000, 8000,
    9000, 10000, 11000, 12000,
    13000, 14000, 15000, 16000
    ])

print(sales)

print("\n------------reshapeing------------\n")

print(sales.reshape(4, 3))

quaterly_sales = sales.reshape(3, 4)

for i in quaterly_sales:
	print(i)
