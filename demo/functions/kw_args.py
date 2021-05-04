def process(*values, **details):
    for v in values:
        print(v)

    for k, v in details.items():
        print(k, v)


process(a=10, b=20, c=100)
process(name="Python", year=1991)

process(10, 20, name="Abc", age=20)
