# Function returning a value
def f1():
    pass


def add(a, b):
    return a + b


def factorial(n: int) -> int:
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact


print(f1())
print(add(10, 20))
print(add('Abc', 'Xyz'))
print(factorial(6))
