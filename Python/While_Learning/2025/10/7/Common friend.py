def common_friends(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    common = set_1.intersection(set_2)
    return common

list_1 = ['Alice', 'Bob', 'Tom']
list_2 = ['Alice', 'Shu', 'Sam']
print(common_friends(list_1,  list_2))