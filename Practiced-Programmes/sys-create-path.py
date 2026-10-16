import sys

print("Befor Adding:")
print(sys.path)

sys.path.append("D:\\python\\my_module")

print("\nAfter Adding:")
print(sys.path)

from employee import employee_name
from employee import employee_salary
from employee import employee_department

print(employee_name())
print(employee_salary())
print(employee_department())