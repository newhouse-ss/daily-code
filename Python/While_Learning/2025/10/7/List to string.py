'''
def list_to_string(lst):
    for c in lst:
        c = str(c)#c只是一个临时变量？无法改变lst，通过调用数组的形式改变
        print(type(c))
    print(lst)
    print(type(lst[0]))

list_to_string([1, 2, 3])
'''

def list_to_string(lst):
    for c in range(len(lst)):
        lst[c] = str(lst[c])
        print(type(lst[c]))
    print(lst)
    return ''.join(lst)

print(list_to_string([1, 2, 3]))