class A:
    def __init__(self, p1):
        pass


class B:
    def __init__(self, p2):
        pass


class C(A, B):
    def __init__(self, p1, p2):
        A.__init__(self, p1)
        B.__init__(self, p2)


obj = C(10, 20)
