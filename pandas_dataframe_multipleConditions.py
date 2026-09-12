import pandas as pd  

ecommerce_data = {
	"Product": ["Laptop", "Mobile", "Headphones", "Keyboard", "Monitor", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "Price": [60000, 35000, 2500, 1800, 15000, 1200],
    "Quantity": [2, 5, 10, 8, 3, 15],
    "Rating": [4.5, 4.2, 4.0, 3.8, 4.6, 4.1]
}

product_df = pd.DataFrame(ecommerce_data)

print(product_df)

Top_Prducts = product_df[(product_df["Price"] > 20000) & (product_df["Rating"] >= 4.2)]

Top_electronics = product_df[(product_df["Category"] == "Electronics") | (product_df["Rating"] >= 4.5)]

electronics_products = product_df[(product_df["Price"] > 2000) & ((product_df["Category"] == "Electronics") | (product_df["Rating"] >= 4.5))]

print("----------------Multiple_Conditions-----------------")

print("Top Products :", Top_Prducts)
print("Top Electronic Products:", Top_electronics)
print("Electioncs Products:", electronics_products)