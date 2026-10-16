def student(**details):

    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Department:", details["department"])
    print(details)

student(name="Jagan", age=21, department="MPC")