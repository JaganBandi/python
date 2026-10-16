import pandas as pd  

import matplotlib.pyplot as plt  

restaurant_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Orders": [300, 350, 320, 410, 450, 500],
    "Revenue": [90000, 105000, 96000, 123000, 135000, 150000]
}

restaurant_df = pd.DataFrame(restaurant_data)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)

plt.plot(
	restaurant_df["Month"],
	restaurant_df["Orders"],
	marker="o"
	)

plt.title("Monthly Orders")

plt.subplot(1, 2, 2)
plt.plot(
	restaurant_df["Month"],
	restaurant_df["Revenue"],
	marker="o"
	)



plt.show()