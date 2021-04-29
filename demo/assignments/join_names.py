names = []
while True:
    s = input("Enter the string [end to stop] :")
    if s == 'end':
        break
    names.append(s)

print(':'.join(names))
