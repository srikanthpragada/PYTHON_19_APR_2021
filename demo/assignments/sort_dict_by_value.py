def take_second(t):
    return t[1]


d = {1: 20, 3: 10, 4: 50, 2: 15}

for k, v in sorted(d.items(), key=take_second):
    print(k, v)

for k, v in sorted(d.items(), key=lambda t: t[1]):
    print(k, v)
