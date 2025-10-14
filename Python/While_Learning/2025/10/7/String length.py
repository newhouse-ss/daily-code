def string_len(strg):
    length = len(strg)
    reversed_str = reversed(strg)#reversed 返回的是一个迭代器，需要用''.join()重新生成字符串
    print(length, ''.join(reversed_str))

string_len("Shu")