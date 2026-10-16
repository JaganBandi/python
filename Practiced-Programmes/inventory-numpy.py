import numpy as np  

inventory = np.array([
	50, 60, 70,
    80, 90, 100,
    110, 120, 130,
    140, 150, 160,
    170, 180, 190,
    200, 210, 220
    ])

store_inventory = inventory.reshape(3, -1)

print(store_inventory)

