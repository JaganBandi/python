import pandas as pd  

orders = {
	"Order_ID": [101, 102, 103, 104, 105, 106],
    "Product": ["Laptop", "Phone", "Laptop", "Shoes", "Phone", "Tablet"],
    "Payment": ["UPI", "COD", "UPI", "Card", "COD", "UPI"]
}

orders_df = pd.DataFrame(orders)

print(orders_df)

unique_payments = orders_df["Payment"].unique()

print(unique_payments)