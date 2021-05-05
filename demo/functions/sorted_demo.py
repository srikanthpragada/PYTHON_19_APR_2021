# sorted() demo

def take_number(code):
    return code[2:]


nums = [10, -20, - 4, 5, -11]
names = ['Java', 'Python', 'C#', 'Cobol', 'SQL']
codes = ['AB3939', 'BB39393', 'XY18182', 'PD39383', 'BB392911']

for n in sorted(nums, key=abs):
    print(n)

for n in sorted(names, key=len):
    print(n)

for n in sorted(codes, key=take_number):
    print(n)
