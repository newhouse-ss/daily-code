from string import ascii_letters
from random import choice

pwd_lst = []

for i in range(10):
    a = choice(ascii_letters)
    pwd_lst.append(a)

pwd = ''.join(pwd_lst)
print(pwd)