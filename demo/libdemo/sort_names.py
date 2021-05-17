# Take names from names.txt and display them in sorted order

f = open("names.txt", "rt")

for line in sorted(set(f.readlines())):
    line = line.strip()
    if len(line) > 0:
        print(line)

f.close()
