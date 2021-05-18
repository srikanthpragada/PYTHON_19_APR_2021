# Take names from names.txt and display them


with open("names.txt", "rt") as f:
    for line in f.readlines():
        print(line.strip())

