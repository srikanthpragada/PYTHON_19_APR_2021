nums = [10, 20, 30, 35, 43, 21, 38, 90, 23, 40]


def iseven(n):
    return n % 2 == 0


for n in filter(iseven, nums):
    print(n)

for c in filter(str.isupper, "How Is This"):
    print(c)
