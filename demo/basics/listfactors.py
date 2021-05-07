# Display factors for the number given on command line
import sys

if len(sys.argv) < 2:
    print("Usage : python listfactors.py number")
    exit()

num = int(sys.argv[1])

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(i, end=' ')

