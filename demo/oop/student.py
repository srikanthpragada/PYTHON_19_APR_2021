class Student:
    # Class attribute or Static attributes
    courses = {"Python": 5000, "DS": 10000, "DL": 12000}

    @staticmethod
    def getfee(course):
        return Student.courses[course]

    @classmethod
    def createPythonStudent(cls, name):
        return cls(name)

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

    def totalfee(self):
        return Student.courses[self.course]

    def getdue(self):
        return self.totalfee() - self.feepaid

    @property  # getter method
    def balance(self):
        return self.totalfee() - self.feepaid


print(Student.getfee("DS"))  # static method
ps = Student.createPythonStudent("Van")
ps.display()
print(ps.balance)

#
# s1 = Student("Steve")  # Create object and call __init__()
# s1.display()
# s1.payment(5000)
# s1.display()
#
# s2 = Student("Bob", "DS")
# s2.display()
