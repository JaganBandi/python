import pandas as pd  

products = {
	"Product_ID" : [101, 102, 103, 104, 105, 106, 107, 108],
	"Product" : ["Laptop", "Phone", "Shirt", "Shoes", "Tabelt", "Jeans", "Watch", "HeadPhones"],
	"Category" : ["Electronics", "Electronics", "Fashion", "Fashion", "Electronics", "Fashion", "Accessories", "Electronics"]
}

products_df = pd.DataFrame(products)

print(products_df.nunique())