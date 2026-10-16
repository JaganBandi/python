person1 = {
    "name": "Hymavathi",
    "age": 27,
    "gender": "female"
}

person2 = {
    "name": "Maneesha",
    "age": 25,
    "gender": "female"
}

person3 = {
    "name": "Jagan",
    "age": 21,
    "gender": "male"
}

person4 = {
    "name": "Malleswarramma",
    "age": 40,
    "gender": "female"
}

person5 = {
    "name": "Peddaiah",
    "age": 47,
    "gender": "male"
}

myfamily = {
    "person1": person1,
    "person2": person2,
    "person3": person3,
    "person4": person4,
    "person5": person5
}

print(myfamily)

print(myfamily["person3"]["name"])
print(myfamily["person4"]["age"])

for person, details in myfamily.items():

    print(person)

    for key, value in details.items():

        print(key, ":", value)

    print()