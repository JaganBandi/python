import numpy as np 

prices = np.array([1200, 800, 2500, 1500, 800, 3000, 1200, 4500])

print("Original Prices:", prices)

sorted_prices = np.sort(prices)
print("Sorted Prices:", sorted_prices)

uniques_prices = np.unique(prices)
print("Unique Prices:", uniques_prices)

discount = 200

discount_prices = prices - discount
print("Discount Prices:", discount_prices)

prices_copy = discount_prices.copy()
prices_copy[0] = 500 

print("Copy Prices:", prices_copy)

random_prices = np.random.choice(prices, 3)
print("Random Prices:", random_prices)


