# Varying number of arguments
def wish(*names, message="Hello"):
    for n in names:
        print(message, n)


wish("Andy", "Joe", "Scott")
wish("Larry", "Sergy", message="Hi")
