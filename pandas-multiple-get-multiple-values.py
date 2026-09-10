import pandas as pd  

product_prices = pd.Series([55000, 25000, 30000, 18000, 2000],
	index=["Laptop", "Mobile", "Tablet", "HeadPhones", "Keyboard"])

print(product_prices.to_frame(name="Price"))
print("Label Based:", product_prices.loc[["Laptop", "Tablet", "Keyboard"]])
print("Position Based:", product_prices.iloc[[1,3]])

