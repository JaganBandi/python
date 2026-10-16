import numpy as np   

orders = np.array([101, 102, 101, 104, 103, 102, 105, 101, 104])

unique_orders = np.unique(orders)

print("All Orders :", orders)

print("Unique Orders:", unique_orders)