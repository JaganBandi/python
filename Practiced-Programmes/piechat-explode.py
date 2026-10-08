import pandas as pd 

import matplotlib.pyplot as plt 

sales_data = {
    "Brand": [
        "Samsung",
        "Apple",
        "OnePlus",
        "Xiaomi",
        "Vivo"
    ],
    "Units_Sold": [2500, 3200, 1500, 2200, 1800]
}

sales_df = pd.DataFrame(sales_data)

plt.figure(figsize=(10, 6))
explode_values = [0, 0.1, 0, 0, 0]

plt.pie(
	sales_df["Units_Sold"],
	labels=sales_df["Brand"],
	autopct="%1.1f%%",
	explode= explode_values
	)

plt.title("Smart Phone Distribution")

plt.tight_layout()
plt.show()