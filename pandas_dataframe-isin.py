import pandas as pd   

Online_products= {
    "Product": ["Laptop", "Mobile", "Headphones", "Keyboard", "Monitor", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "Price": [60000, 35000, 2500, 1800, 15000, 1200],
    "Quantity": [2, 5, 10, 8, 3, 15],
    "Rating": [4.5, 4.2, 4.0, 3.8, 4.6, 4.1]
}


market_df = pd.DataFrame(Online_products)

selected_categories = market_df[market_df["Category"].isin(["Electronics", "Accessories"])]

not_electronics = market_df[~market_df["Category"].isin(["Electronics"])]

product_price  = market_df[market_df["Price"].isin([1200, 2500, 15000])]

condition_result = market_df[(market_df["Category"].isin(["Electronics", "Accessories"])) & (market_df["Rating"] >= 4.2)]

print("-----------------Selected Categoires--------------------")

print("Slected Categories:", selected_categories)
print("Except Product:", not_electronics)
print("Selected Product Prices:", product_price)
print("Condition:", condition_result)
