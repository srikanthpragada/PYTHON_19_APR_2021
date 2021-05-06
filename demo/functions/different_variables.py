g = 1000  # Global variable


def f1():
    a = 100  # Enclosing variable
    print("f1()", g, a)

    # Local function
    def f2():
        b = 200  # Local variable
        a = 1
        print("f2()", g, a, b)

    f2()
    print("After f2()", a)


f1()
