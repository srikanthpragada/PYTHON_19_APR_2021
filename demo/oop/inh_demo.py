class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(self.name)
        print(self.email)


class Player(Person):
    def __init__(self, name, email, game):
        super().__init__(name, email)
        self.game = game

    def display(self):  # Overriding
        super().display()
        print(self.game)


p = Player('Dhoni', "dhoni@gmail.com", "Cricket")
p.display()

print(isinstance(p, Player))
print(isinstance(p, Person))
print(issubclass(Player, Person))
print(issubclass(Player, Person))
print(issubclass(Person, object))
print(issubclass(str, Person))
print(issubclass(str, object))
