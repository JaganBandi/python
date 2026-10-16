class Organization:

    def __init__(self, organization_name):
        self.organization_name = organization_name


class Department(Organization):

    def __init__(self, organization_name, department_name):
        super().__init__(organization_name)
        self.department_name = department_name


class Employee(Department):

    def __init__(self, organization_name, department_name, employee_name):
        super().__init__(organization_name, department_name)
        self.employee_name = employee_name


class Salary(Employee):

    def __init__(self, organization_name, department_name, employee_name, salary):
        super().__init__(organization_name, department_name, employee_name)
        self.salary = salary

    def display(self):
        print("Organization:", self.organization_name)
        print("Department:", self.department_name)
        print("Employee:", self.employee_name)
        print("Salary:", self.salary)


s1 = Salary("Microsoft", "IT", "Jagan", 50000)

s1.display()

