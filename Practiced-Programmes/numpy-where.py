import numpy as np  

transactions = np.array([500, 2500, 1200, 5000, 800, 3200])

print(transactions)

transaction_type = np.where(transactions >= 2000, "Large Transaction", "Small Transaction")

print("Trasaction Type:", transaction_type)
