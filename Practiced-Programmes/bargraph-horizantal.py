import pandas as pd  

import matplotlib.pyplot as plt  

department_data = {
    "Department": [
        "Python Development",
        "DevOps Engineering",
        "Data Analysis",
        "Software Testing",
        "Cloud Engineering"
    ],
    "Employees": [25, 18, 22, 15, 20]
}

department_df = pd.DataFrame(department_data)

plt.figure(figsize=(10, 6))

plt.barh(
	department_df["Department"],
	department_df["Employees"],
	)

plt.title("Employees by Department")
plt.xlabel("Number of Employees")
plt.ylabel("Department")

plt.tight_layout()
plt.show()