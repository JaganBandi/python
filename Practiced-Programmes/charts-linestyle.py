import pandas as pd 

import matplotlib.pyplot as plt  

car_sales = {
	 "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Cars_Sold": [45, 52, 48, 65, 72, 80]
}

cars_df = pd.DataFrame(car_sales)

plt.plot(
	cars_df["Month"],
	cars_df["Cars_Sold"],
	marker="o",
	linestyle= ":"
	)

plt.title("Monthly Car Sales")
plt.xlabel("Month")
plt.ylabel("Car Sold")
plt.show()