# Positional-only arguments
def wish(name, mes, /):
    print(mes, name)


wish("Joe", "Hi")
# wish(message="Hello", name="Scott")
