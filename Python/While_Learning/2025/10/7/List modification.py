def list_modify(list):
    list_copy = list.copy()
    new = input('Input what you want: ')
    list_copy.append(int(new))
    return list_copy
lst = [2, 3, 5]
print(list_modify(lst))
print(lst)