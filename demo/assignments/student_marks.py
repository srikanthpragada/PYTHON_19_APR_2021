data = {"Joe": "50,66,80",
        "Bob": "87,86,90",
        "Jack": "45,45,36"}

for name, marks in sorted(data.items()):
    marks = marks.split(",")
    total = sum(map(int, marks))
    print(f"{name:10} {total:3}")
