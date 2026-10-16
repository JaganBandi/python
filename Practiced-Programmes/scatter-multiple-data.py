import pandas as pd  

import matplotlib.pyplot as plt 

laptop_data = {
    "Price": [40000, 50000, 60000, 70000, 80000],
    "Sales": [120, 100, 85, 65, 50]
}

phone_data = {
    "Price": [10000, 15000, 20000, 25000, 30000],
    "Sales": [300, 260, 220, 180, 140]
}

laptop_df = pd.DataFrame(laptop_data)
phone_df = pd.DataFrame(phone_data)


plt.scatter(
	laptop_df["Price"],
	laptop_df["Sales"],
	label="Laptops",
	color="blue"
	)

plt.scatter(
	phone_df["Price"],
	phone_df["Sales"],
	label="Phones",
	color="red"
	)

plt.title("Product Price VS Sales")

plt.xlabel("Price")
plt.ylabel("Units_Sold")
plt.legend()

plt.show()