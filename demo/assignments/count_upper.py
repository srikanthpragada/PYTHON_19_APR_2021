st = "This Is OKAY"

count = 0
for c in st:
    if c.isupper():
        count += 1

print(f"No. of uppercase letters : {count}")
