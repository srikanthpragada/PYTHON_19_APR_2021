st = "This is to test a program and test is to check"

words = st.split(" ")
for w in sorted(set(words)):
    print(f"{w} - {words.count(w)}")

