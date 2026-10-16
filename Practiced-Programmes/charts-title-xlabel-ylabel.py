import pandas as pd  
import matplotlib.pyplot as plt  

food_sales = {
	"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Orders": [120, 150, 135, 180, 210, 240]
}

food_df = pd.DataFrame(food_sales)

plt.plot(food_df["Month"], food_df["Orders"])

plt.title("Monthly Food Delivary Orders")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.show()