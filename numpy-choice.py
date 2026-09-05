import numpy as np  

students = np.array(["Jagan", "Harini", "Shiva", "Venky"])

selected_students = np.random.choice(students, 2)

print(selected_students)