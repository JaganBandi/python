import numpy as np  

attendence = np.array([
	 1, 1, 0, 1, 1, 0,
     1, 1, 1, 0, 1, 1,
     0, 1, 1, 1, 0, 1,
     1, 0, 1, 1, 1, 0
    ])


attendence = attendence.reshape(4, -1)

print(attendence)

for department_attendence in attendence:
	print(department_attendence)


