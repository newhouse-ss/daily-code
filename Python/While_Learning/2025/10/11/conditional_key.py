diction = {"alice":15}
for key in diction.keys():
    key_value = diction[key]
    key_list = list(key)
    if key_list[0] == 'a':
        print(key_list[0])
        key_list[0] = key_list[0].upper()
        print(key_list[0])
        new_key = ''.join(key_list)
    diction[new_key] = key_value
print(diction)