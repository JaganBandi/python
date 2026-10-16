import sys

print(sys.path)

from company.employee import employee_name
from company.department import employee_department
from company.department import employee_location
from company.salary import employee_salary

print(employee_name())
print(employee_department())
print(employee_location())
print(employee_salary())
