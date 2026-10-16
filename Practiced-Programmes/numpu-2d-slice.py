import numpy as np  

salaries = np.array([
	[40000, 42000, 45000],
    [35000, 38000, 40000],
    [50000, 52000, 55000],
    [30000, 32000, 35000]
    ])

print(salaries[0:2, 0:2])
print(salaries[:, 0:2])



