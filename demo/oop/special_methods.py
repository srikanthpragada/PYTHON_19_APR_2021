class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email

    def __gt__(self, other):
        return self.name > other.name


p1 = Person("Abc", "abc@gmail.com")
p2 = Person("Abc", "abc@gmail.com")
p3 = Person("Xyz", "xyz@gmail.com")
print(p1)  # p1.__str__()
print(str(p1))
print(p1.__str__())

print(p1 == p2)  # p1.__eq__(p2)
print(p3 > p2)   # p1.__gt__(p2)