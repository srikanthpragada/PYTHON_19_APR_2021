# Display table for the given number and length
import sys

if len(sys.argv) < 2:
    print("Usage : python table.py number [length]")
    exit()

if len(sys.argv) > 2:
    length = int(sys.argv[2])  # Length
else:
    length = 10

num = int(sys.argv[1])

for i in range(1, length + 1):
    print(f"{num:3} * {i:2} = {i * num :5}")
