import random
import string

chars = string.punctuation+string.ascii_letters+string.digits
chars = list(chars)
key = chars.copy()
random.shuffle(key)
print(chars)
print(key)

def main():
    plain_chars = input("Input your original chars: ")
    encrypted_chars = ''
    for letter in plain_chars:
        index = chars.index(letter)
        encrypted_chars += key[index]
    print(f"Original chars: {plain_chars}")
    print(f"Encrypted chars: {encrypted_chars}")
if __name__ == '__main__':
    main()