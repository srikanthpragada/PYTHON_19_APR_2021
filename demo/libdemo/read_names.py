# Take names from names.txt and display them

f = open("names.txt", "rt")

for line in f.readlines():
    print(line.strip())

f.close()
