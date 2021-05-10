class Player:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private


p1 = Player("Abc", 23)
print(p1._Player__age)
p1.gender = "Male"
print(p1.__dict__)
