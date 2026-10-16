import pandas as pd  
import matplotlib.pyplot as plt 

phone_sales = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Units_Sold": [120, 145, 135, 170, 190, 220]
}

phone_df = pd.DataFrame(phone_sales)


plt.plot(
	phone_df["Month"],
	phone_df["Units_Sold"],
	marker="o",
	linestyle="-",
	color="blue",
	label="SmartPhones Sales",
	)

plt.title("Monthly Smartphone Sales")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend()
plt.grid()

plt.show()
