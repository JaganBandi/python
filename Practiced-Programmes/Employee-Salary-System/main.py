import employee as emp

name = input("Enter Your Name:")
basic_salary = int(input("Enter Your Salary:"))
bonus = int(input("Enter Your Bonus:"))
tax = int(input("Enter Your tax:"))

emp.employee_details(name)

gross_salary = emp.gross_salary(basic_salary, bonus)
print("Gross Salary:", gross_salary)

net_salary = emp.net_salary(gross_salary, tax)
print("Net Salary:", net_salary)