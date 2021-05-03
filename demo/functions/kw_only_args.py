# Keyword-only arguments
def wish(*, message, name):
    print(message, name)


# wish("Joe", "Hi")
wish(name="Scott", message="Hello")
wish(message="Hello", name="Scott")
