import pandas as pd  

import matplotlib.pyplot as plt 

car_a = {
	 "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [45, 52, 48, 65, 72, 80]
}

car_b = {
	"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [40, 48, 55, 60, 68, 75]
}

car_a_df = pd.DataFrame(car_a)
car_b_df = pd.DataFrame(car_b)

plt.plot(
	car_a_df["Month"],
	car_a_df["Sales"],
	label="Model A",
	marker="o",
	color="red"
	)

plt.plot(
	car_b_df["Month"],
	car_b_df["Sales"],
	label="Model B",
	marker="s",
	color="green",
	linestyle="--"
	)

plt.title("Monthly Car Sales Comparision")
plt.xlabel("Month")
plt.ylabel("Cars Sold")
plt.legend()
plt.show()