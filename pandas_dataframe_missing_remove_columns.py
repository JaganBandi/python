import pandas as pd  


products = {
    "Product": ["Laptop", "Mobile", "Mouse", "Keyboard"],
    "Category": ["Electronics", None, "Accessories", "Accessories"],
    "Price": [60000, 35000, None, 1800],
    "Rating": [4.5, 4.2, 4.1, None]
}


product_df = pd.DataFrame(products)

print("Original Data:", product_df)

Cleaned_product = product_df.dropna(axis=1)

print("Cleaned Data:", Cleaned_product)