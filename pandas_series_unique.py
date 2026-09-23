import pandas as pd  


products = pd.Series([
         "Laptop", "Phone", "Laptop", "Shoes", "Phone", "Tablet", "Shoes"	
])

print("Original Series :", products)

products_unique_values = products.unique()


print("Unique Values:", products_unique_values)