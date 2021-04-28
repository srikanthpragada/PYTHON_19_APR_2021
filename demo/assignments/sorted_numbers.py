# Print given numbers in sorted order
numbers = []
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
    numbers.append(num)

for n in sorted(numbers):
    print(n)

