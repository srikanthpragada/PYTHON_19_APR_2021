# Display avg of positive numbers until 0 is given

count = total = 0
while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    if num < 0:
        continue

    total += num
    count += 1

print(f"Average = {total//count}")
