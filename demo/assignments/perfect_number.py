
num = int(input("Enter a number :"))
total = 1

for i in range(2, num//2 + 1):
    if num % i == 0:
        total += i

if total == num:
    print("Perfect Number")
else:
    print("Not perfect number")
