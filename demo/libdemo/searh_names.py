# Take names from names.txt and display them

searchword = input("Enter name :")

f = open("names.txt", "rt")

for line in f:
    if line.find(searchword) >= 0:
        print(line, end='')

f.close()
