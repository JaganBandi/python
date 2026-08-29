import numpy as np  

performance = np.array([
	[85, 90, 88],
    [70, 75, 80],
    [92, 95, 90],
    [65, 72, 78]
    ])

print(performance[-1])
print(performance[-2, 1])
print(performance[-3, 0])
print(performance[-4, 2])