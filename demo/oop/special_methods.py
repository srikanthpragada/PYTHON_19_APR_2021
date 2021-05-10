class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"


p1 = Person("Abc", "abc@gmail.com")
p2 = Person("Abc", "abc@gmail.com")
print(p1)  # p1.__str__()
print(str(p1))
print(p1.__str__())

print(p1 == p2)