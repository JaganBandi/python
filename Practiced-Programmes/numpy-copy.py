import numpy as np  

numbers = np.array([5, 10, 15, 20])

numbers_copy = numbers.copy()

numbers_copy[1] = 100

print("Original Numbers:", numbers)
print("Numbers Copy    :", numbers_copy)