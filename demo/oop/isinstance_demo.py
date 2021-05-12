def add(a, b):
    if isinstance(a, list):
        l = []
        for v1, v2 in zip(a, b):
            l.append(v1 + v2)
        return l

    if isinstance(a, str):
        a = int(a)

    if isinstance(b, str):
        b = int(b)

    return a + b


print(add(10, 20))
print(add('10', '20'))
print(add('100', 200))
print(add([10, 20], [200, 300]))
