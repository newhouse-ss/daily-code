dictionary = {"a": 1, "b": 2}
rev_dictionary = {}
for item in dictionary.items():
    a = item[0]
    b = item[1]
    a, b = b, a
    rev_dictionary[a] = b
    print(rev_dictionary)