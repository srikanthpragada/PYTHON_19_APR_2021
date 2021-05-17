# Take names from user until end and write names to names.txt

f = open("names.txt", "wt")

while True:
    name = input("Enter a name [end to stop] :")
    if name == 'end':
        break

    f.write(name + "\n")

f.close()
