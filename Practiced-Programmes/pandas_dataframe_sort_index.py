import pandas as pd  

products = {
    "Product": ["Laptop", "Mobile", "Monitor", "Keyboard", "Mouse"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
    "Price": [60000, 35000, 15000, 1800, 1200]
}


product_df = pd.DataFrame(products, index=[105, 101, 104, 102, 103])

print("Original DataFrame:", product_df)

Ascending_index = product_df.sort_index()

print("Ascending Order:", Ascending_index)

Descending_order = product_df.sort_index(ascending=False)

print("Decending Order:", Descending_order)

