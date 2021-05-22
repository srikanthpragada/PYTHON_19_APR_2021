import re

f = open("phones.txt", "rt")

phones = []

for line in f:
    numbers = re.findall(r"\d+", line)
    for n in numbers:
        if len(n) == 10:
            phones.append(n)

f.close()

for n in sorted(phones):
    print(n)
