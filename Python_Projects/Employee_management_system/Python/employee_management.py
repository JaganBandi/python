class Employee:
	def __init__(self, emp_id, name, department, salary):
		self.emp_id = emp_id
		self.name = name
		self.department = department
		self.__salary = salary

	def display_details(self):
		print("Employee ID:", self.emp_id)
		print("Employee Name:",self.name)
		print("Employee Department:",self.department)
		print("Employee Salary:",self.__salary)

	def get_salary(self):
		return self.__salary

	def set_salary(self, new_salary):
		if new_salary > 0:
			self.__salary = new_salary

		else:
			print("Invalid Salary")

employee1 = Employee(101, "Ravi", "Python", 45000)
employee2 = Employee(102, "Suresh", "DevOps", 55000)

employees = [employee1, employee2]

emp_id = int(input("Enter Employee ID:"))
name = input("Enter Your Name:")
department = input("Enter Department:")
salary = int(input("Enter Your Salary:"))

new_employee = Employee(emp_id, name, department, salary)
employees.append(new_employee)

print("Total Employees:", len(employees))

for employee in employees:
	employee.display_details()
	print("-------------------")

search_id = int(input("Enter Employee ID to search: "))
found = False

for employee in employees:
	if employee.emp_id == search_id:
		employee.display_details()
		found = True
		break

if not found:
	print("Employee not Found")

update_id = int(input("Enter Employee ID to Update Salary: "))

found = False

for employee in employees:
	if employee.emp_id == update_id:
		new_salary = int(input("Enter New Salary: "))
		employee.set_salary(new_salary)
		print("Current Salary:", employee.get_salary())
		found = True
		break

if not found:
	print("Employee Not Found")

delete_id = int(input("Enter Employee ID to Delete: "))

found = False

for employee in employees:
	if employee.emp_id == delete_id:
		employees.remove(employee)
		print("Employee Deleted SuccessFully")
		found = True
		break

if not found:
	print("Employee not Found")

print("Total Employees:", len(employees))
