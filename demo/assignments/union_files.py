f = open("names.txt", "rt")
first_lines = f.readlines()
f.close()

f = open("names2.txt", "rt")
second_lines = f.readlines()
f.close()

common_lines = []
for line in first_lines:
    if line in second_lines and line not in common_lines:
        print(line, end = '')
        common_lines.append(line)
