class Student:
    # Constructor
    def __init__(self, name, course="Python"):
        # Object Attributes
        self.name = name
        self.course = course
        self.feepaid = 0

        # Methods

    def display(self):
        print(self.name)
        print(self.course)
        print(self.feepaid)

    def payment(self, amount):
        self.feepaid += amount


s1 = Student("Steve")  # Create object and call __init__()
s1.display()
s1.payment(5000)
s1.display()
#
# s2 = Student("Bob", "Data Science")
# s2.display()
