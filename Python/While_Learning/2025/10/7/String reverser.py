def string_reverser(str):
    str_list = str.split()
    new_list = []
    for c in reversed(str_list):
        new_list.append(c)
    return new_list

str = 'Fuck the algorithms'
print(' '.join(string_reverser(str)))