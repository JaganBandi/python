import pandas as pd  
import matplotlib.pyplot as plt  

cars_df = pd.DataFrame({
	 "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Cars_Sold": [45, 52, 48, 65, 72, 80]
	})

plt.plot(
	cars_df["Month"],
	cars_df["Cars_Sold"],
	marker="o"
	)

plt.title("Monthly Car Sales")
plt.xlabel("Month")
plt.ylabel("Cars Sold")
plt.show()
