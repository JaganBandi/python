class Employee:
	def __init__(self, emp_id, name, department, salary):
		if emp_id <= 0:
			raise ValueError("Employee ID Must be Positive")

		if not name.strip():
			raise ValueError("Employee name cannot be empty")

		if not department.strip():
			raise ValueError("Department name cannot be empty")

		if salary <= 0:
			raise ValueError("Salary must be positive")

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

found = False

for employee in employees:
	if employee.emp_id == emp_id:
		print("Employee ID Already Exist")
		found = True
		break

if not found:
	new_employee = Employee(emp_id, name, department, salary)
	employees.append(new_employee)
	print("Employee Added SuccessFully")

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

while True:
	print("\n ---------------Employee Management System ----------------")
	print("1. Add Employee")
	print("2. View All Employee")
	print("3. Search Employee")
	print("4. Update Salary")
	print("5. Delete Employee")
	print("6. Exit")

	choice = input("Enter your choice:" )

	if choice == "1":
		emp_id = int(input("Enter Employee ID:"))
		name = input("Enter Employee Name:")
		department = input("Enter Department:")
		salary = int(input("Enter Salary:"))

		new_employee = Employee(emp_id, name, department, salary)
		employees.append(new_employee)


	elif choice == "2":
		print("View all the employees in the system")

		for employee in employees:
			employee.display_details()
			print("-----------------------")


	elif choice == "3":
    search_id = int(input("Enter Employee ID to search: "))
    found = False

    for employee in employees:
        if employee.emp_id == search_id:
            employee.display_details()
            found = True
            break

    if not found:
        print("Employee Not Found")


	elif choice == "4":
		update_id = int(input("Enter Employee ID to Update Salary: "))
		found = False

		for employees in employees:
			if employee.emp_id == update_id:
				new_salary = int(input("Enter New Salary:"))
				employee.set_salary(new_salary)
				print("Current Salary:", employee.get_salary())
				found = True
				break

		if not found:
			print("Employee Not Found")

	elif choice == "5":
		delete_id = int(input("Enter Employee ID to Delete: "))
		found = False

		for employee in employees:
			if employee.emp_id == delete_id:
				employee.remove(employee)
				print("Employee Deleted SuccessFully")
				found = True
				break

                                      

	elif choice == "6":
		print("Exiting Employee Management System")
		break

	else:
		print("Invalid choice please enter 1-6")





