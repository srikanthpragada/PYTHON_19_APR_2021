# Math functions

def square(n):
    return n * n


def iseven(n):
    """
    Checks whether the given number is even number
    Param n is the number to check
    Returns True or False
    """
    return n % 2 == 0


def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i

    return fact


# Testing
if __name__ == '__main__':
    print('Name : ', __name__)
    print(square(10))
    print(factorial(5))
    print(iseven(10))
