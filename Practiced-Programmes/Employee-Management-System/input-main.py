import employee as emp

name = input("Enter Employee Name:")
company = input("Enter Company Name:")
salary = int(input("Enter Salary:"))
experience = int(input("Enter Experience:"))


emp.employee_details(name, company)
emp.salary(salary)
emp.experience(experience)