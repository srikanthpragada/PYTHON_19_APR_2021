class EvenNumbers_Iterator:
    def __init__(self, start, end):
        self.number = start if start % 2 == 0 else start + 1
        self.end = end

    def __next__(self):
        if self.number > self.end:
            raise StopIteration

        v = self.number
        self.number += 2
        return v


class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return EvenNumbers_Iterator(self.start, self.end)


for n in EvenNumbers(50, 75):
    print(n)
