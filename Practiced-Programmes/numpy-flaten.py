import numpy as np  

performance = np.array([
	 [80, 85, 90],
     [70, 75, 80],
     [90, 95, 88],
     [65, 72, 78]
    ])

print(performance)
print(performance.shape)

flat_performance = performance.flatten()

print(flat_performance)
print(flat_performance.shape)