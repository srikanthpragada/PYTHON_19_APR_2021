def has_upper(st):
    for c in st:
        if c.isupper():
            return True

    return False


def start_with_digit(st):
    return st[0].isdigit()
