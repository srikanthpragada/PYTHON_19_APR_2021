import os

startdir = r"c:\classroom\apr19\demo"

allfiles = os.walk(startdir)
count = 0
for (dirname, dirs, files) in allfiles:
    for filename in files:
        if filename.endswith(".py"):
            print(dirname + "\\" + filename)
            count += 1

print(f"Count = {count}")
