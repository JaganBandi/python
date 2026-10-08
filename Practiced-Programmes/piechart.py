import pandas as pd   

import matplotlib.pyplot as plt  


user_data = {
    "Platform": [
        "Android",
        "iOS",
        "Windows",
        "Web"
    ],
    "Users": [5500, 3000, 500, 1000]
}

user_df = pd.DataFrame(user_data)

plt.pie(
	user_df["Users"],
	labels=user_df["Platform"],
	autopct="%1.1f%%"
	)

plt.title("User Distribution By Platform")

plt.show()