def reverse_str(string):
    r_str = string[-1::-1]
    print(r_str)

def is_palindrome(string):
    pre = 0
    pos = len(string)-1

    while pre<pos and string[pre] == string[pos]:
        pre += 1
        pos -= 1

    if pre>=pos:
        return True
    
    return False

print(is_palindrome('aabbccaaaaccbbaa'))