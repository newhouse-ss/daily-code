def str_length(str):
    return len(str)

string1 = ["I", "am", "so", "anxious", "and", "sad"]
print(str_length(string1))

string1.sort(key = str_length, reverse = True)
print(string1)

str = "Do not ignroe my feeling!!!"
tp = tuple(str)
print(tp)

single_tuple = (42,)
print(single_tuple)
print(type(single_tuple))

my_tuple = (1, 2, 3)
try:
    my_tuple[2] = 5
except TypeError as e:#用于直接打印error信息
    print(f"error: {e}")

try:
    my_tuple.append(55)
except AttributeError as e:
    print(f'error: {e}')

a, b, c = my_tuple
print(a, b, c)