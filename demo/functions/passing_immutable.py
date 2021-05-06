def zero(a):
    print(id(a))
    a = 0
    print(id(a))


n = 100
print(id(n))
zero(n)
print(n)
