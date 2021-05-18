# Remove blank lines from the given file

FILENAME = "names.txt"

f = open(FILENAME, "rt")
lines = []
for line in f:
    if len(line.strip()) > 0:  # non-blank line
        lines.append(line)

f.close()
f = open(FILENAME, "wt")
for line in lines:
    f.write(line)

f.close()
