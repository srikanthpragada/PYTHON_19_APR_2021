persons = {}

while True:
    data = input("Enter name,age [end to stop] :")
    if data == 'end':
        break
    name,age = data.split(",")
    persons[name] = age

for name, age in sorted(persons.items()):
    print(f"{name:15} {age:2}")



