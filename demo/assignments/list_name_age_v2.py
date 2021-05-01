data = ["abc,20", "xyz,40", "pqr,25", "def,30", "abc,30"]

persons = {}
for entry in data:
    name, age = entry.split(",")
    if name not in persons:
       persons[name] = age

for name, age in sorted(persons.items()):
    print(f"{name:15} {age:2}")
