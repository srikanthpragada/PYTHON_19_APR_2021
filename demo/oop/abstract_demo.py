from abc import ABC, abstractmethod


# Abstract class
class Student(ABC):
    @abstractmethod
    def getmarks(self):
        pass


class PythonStudent(Student):
    def getmarks(self):
        return 0


class JavaStudent(Student):
    def getmarks(self):
        return 0


ps = PythonStudent()
