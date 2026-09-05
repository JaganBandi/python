import numpy as np  

marks = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [90, 95, 88],
    [65, 72, 78]
   ])

print("Shape:", marks.shape)

student_performance = marks.transpose()

print(student_performance)

print("Shape:", student_performance.shape)