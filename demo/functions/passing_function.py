def math_op(a, b, op):
    print(op(a, b))


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


math_op(10, 20, add)
math_op(20, 10, multiply)
# math_op(10,10, len)   --> Invalid as function must take 2 params

