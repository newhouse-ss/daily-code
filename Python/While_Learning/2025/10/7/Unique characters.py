def unique_characters(str):
    unique_chars = set(str.lower().split())
    return unique_chars

str = 'i i i i i i i i iiiii'
print(unique_characters(str))