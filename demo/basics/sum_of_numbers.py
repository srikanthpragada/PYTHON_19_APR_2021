# Take numbers until 0 is given and display sum of numbers

num = int(input("Enter number [0 to stop] :"))
total = 0
while num != 0:
    total += num
    num = int(input("Enter number [0 to stop] :"))

print(f"Total = {total}")
