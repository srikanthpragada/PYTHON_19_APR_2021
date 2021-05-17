
class EvenNumbers_Iterator:
    def __init__(self):
        self.number = 2

    def __next__(self):
        if self.number > 100:
            raise StopIteration

        v = self.number
        self.number += 2
        return v

class EvenNumbers:
    def __iter__(self):
        return EvenNumbers_Iterator()


for n in EvenNumbers():
    print(n)

