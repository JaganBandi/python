import pandas as pd 
import matplotlib.pyplot as plt 

store_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Customers": [500, 620, 580, 700, 760, 850],
    "Revenue": [150000, 186000, 174000, 210000, 228000, 255000]
}

store_df = pd.DataFrame(store_data)

plt.subplot(1, 2, 1)

plt.plot(
	store_df["Month"],
	store_df["Customers"],
	marker="o",
	)

plt.title("Monthly Customers")
plt.grid()

plt.subplot(1, 2, 2)

plt.plot(
	store_df["Month"],
	store_df["Revenue"],
	marker="o"
	)

plt.title("Monthly Revenue")

plt.grid()

plt.show()

