import matplotlib.pyplot as plt

marks = [35, 40, 45, 48, 50, 55, 60, 65, 70, 72,
         75, 80, 82, 85, 90, 95]

plt.hist(
    marks,
    bins=5,
    range=(45, 90),
    color="green",
    edgecolor="black",
    histtype="step",
    density="True"
    )

plt.title("Student Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")

plt.show()
