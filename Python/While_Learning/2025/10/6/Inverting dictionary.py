def invert_dict(dictionary):
    c_dict = {}
    for key in dictionary:
        c_dict[dictionary[key]] = key
    return c_dict
A_num = {'A':1, 'B':2, 'C':3}
result = invert_dict(A_num)
print(result)