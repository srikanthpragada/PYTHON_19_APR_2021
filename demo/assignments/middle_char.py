st = "Python3"

l = len(st)
if l % 2 == 0:
    l = l // 2
    print(st[l - 1:l + 1])
else:
    print(st[l // 2])
