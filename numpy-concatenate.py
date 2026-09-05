import numpy as np  

morning_orders = np.array([201, 202, 203])
evening_orders = np.array([204, 205, 206])

total_orders = np.concatenate((morning_orders, evening_orders))

print(total_orders)