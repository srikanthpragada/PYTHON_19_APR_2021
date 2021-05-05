names = ['Java', 'Python', 'C#', 'Cobol', 'SQL']

ages = ['20', '34', '44', '23', '19', '9']

for v in map(str.upper, names):
    print(v)

int_ages = map(int, ages)
avg_age = sum(int_ages) / len(ages)
print(avg_age)
