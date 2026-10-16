import pandas as pd   

products = {
	"Product" : ["Laptop", "Mobile", "Tablet", "Keyboard"],
	"Price"   : [55000, 25000, 18000, 1300],
	"Quantity" : [5, 10, 2, 3]
}

product_df = pd.DataFrame(products)

print(product_df)