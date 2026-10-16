import pandas as pd 
import matplotlib.pyplot as plt 

product_data = {
    "Price": [100, 150, 200, 250, 300],
    "Sales": [500, 450, 400, 330, 250]
}

product_df = pd.DataFrame(product_data)

plt.scatter(product_df["Price"],
	product_df["Sales"],
	label="Product Sales"
	)

plt.title("Product VS Sales")
plt.xlabel("Price")
plt.ylabel("Sales")

plt.legend()

plt.show()
