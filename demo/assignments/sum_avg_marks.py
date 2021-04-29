marks = [[89, 37, 87], [56, 66, 77, 88], [34, 55, 67]]

for row in marks:
    total = sum(row)
    avg = total / len(row)
    print(f"{total:3} {avg:2.2f}")
