f = open("marks.txt", "rt")
students = {}

for line in f:
    parts = line.split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    marks = [int(v) for v in parts[1:] if v.strip().isdigit()]
    print(marks)
    avg_marks = sum(marks) / len(marks)
    students[name] = avg_marks

f.close()

for name, avg in sorted(students.items(), key=lambda t: t[1], reverse=True):
    print(f"{name:10} {avg:3.2f}")
