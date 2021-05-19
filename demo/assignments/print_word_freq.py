f = open("text.txt", "rt")

word_freq = {}

for line in f:
    # print(line.split(" "))
    words = [w for w in line.strip().split(" ") if len(w) > 0]  # strip all spaces
    for w in words:
        if w in word_freq:  # word found in dict
            word_freq[w] = word_freq[w] + 1  # inc count
        else:
            word_freq[w] = 1  # Add with count 1

f.close()

for w, count in word_freq.items():
    print(f"{w:10} {count:3}")
