def hasdigit(s):
    for c in s:
        if c.isdigit():
            return True
        
    return False


names = ["Java16", 'Python 3.9', 'C#', 'JavaScript']

for n in filter(hasdigit, names):
    print(n)
