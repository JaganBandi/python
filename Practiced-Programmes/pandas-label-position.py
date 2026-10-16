import pandas as pd  

product_prices = pd.Series([1200, 2500, 1800, 3200],
	index=["Laptop", "Mobile", "Tablet", "Headphones"])

print("Mobile Price:", product_prices.loc['Mobile'])
print("Position Price:", product_prices.iloc[1])