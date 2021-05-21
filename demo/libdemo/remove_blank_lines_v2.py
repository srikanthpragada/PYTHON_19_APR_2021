# Remove blank lines from the given file
import os

FILENAME = "names.txt"
TEMPFILE = "temp.txt"

with open(FILENAME, "rt") as sf, open(TEMPFILE, "wt") as tf:
    for line in sf:
        if len(line.strip()) > 0:  # non-blank line
            tf.write(line)

# Delete source file
os.remove(FILENAME)
os.rename(TEMPFILE, FILENAME)
