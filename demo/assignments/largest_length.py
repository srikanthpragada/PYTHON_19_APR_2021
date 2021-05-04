
def largest_length(*strings):
    ls = strings[0]  # First string is largest string
    for s in strings[1:]:
        if len(s) > len(ls):
            ls = s

    return ls


print( largest_length("Abc","Xy","Pqrs",'Def','Deff'))