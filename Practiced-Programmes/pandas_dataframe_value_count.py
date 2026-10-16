import pandas as pd  

sales = {
	"Bill_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    "Product": ["Rice", "Milk", "Rice", "Sugar", "Milk", "Rice", "Oil"],
    "Quantity": [2, 1, 3, 2, 1, 5, 2]
}

sales_df = pd.DataFrame(sales)

print("Before Count Values:",)
print(sales_df)

product_counts = sales_df["Product"].value_counts()


print("AFter Count Product Values:",)
print(product_counts)