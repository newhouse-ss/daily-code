import helper
import my_module
import greeting
class DOG:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Woof")
def greet(name):
    helper.helper_function()
    print(f"Hello, {name}!")
def square(a):
    """
    The type of a is float.
    """
    return a*a

def c_to_f(Celsius):
    return (Celsius*9/5+32)

def compare(num1, num2):
    if num1 > num2:
        return "greater than"
    elif num1 < num2:
        return "smaller than"
    else:
        return "equal"

def check(str1):
    if str1 == "Python":
        return True
    else:
        return False

def eligible_to_vote(age):
    if age > 18:
        return True
    return False

def all_over_zero(num1, num2, num3):
    if num1>0 and num2>0 and num3>0:
        return True
    return False

def greeting_creater():
    first_name = input("Please give me your first name:")
    last_name = input("Please give me your last name:")
    print(f"Good night! {first_name} {last_name}")

def address_formatter():
    street_address = input("Your street's No.: ")
    city = input("City name: ")
    ken = input("Which ken?: ")
    zip_code = input("Zip Code: ")
    return street_address+", "+city+", "+ken+", "+zip_code
def extract_initials():
    full_name = input("please input your full name: ")
    list_of_name = full_name.split(' ')
    print(list_of_name)
    first_name = list_of_name[0][0]
    last_name = list_of_name[1][0]
    print(first_name+last_name)

def reverse_words():
    str = input("Please input sentence: ")
    str = str[-1::-1]
    print(str)
def palindrome_check():
    sentence = input()
    sentence_1 = sentence[-1::-1]
    if sentence == sentence_1:
        return True
    return False

def personalized_greeting():
    name = input("name:")
    favorite_color = input("color")
    print(f"Hello! {name}, whose favorite color is: {favorite_color}")
str = input("Please input sentence: ")
str = str[-1::-1]
print(str)
#if __name__ == "__main__":#只有文件名等于'main'的时候才会执行如下运算，因为有可能该函数会被别的file调用，在另外的file下，也许只有greet function被需要，不需要打印函数名以及用户输入这些后续操作。
    #print(f"The __name__ variable in maun.py is: {__name__}")
    #user_name = input("Input your name here:")
    #greet(user_name)

#my_module.add(1, 5)
#my_module.hello("Shu")

#my_dog = DOG("Xue Qiu", "fox")
#print(my_dog.name, my_dog.breed)
#my_dog.bark()
#print(square(8))
"""
p1 = greeting.Woman("Mary")#新建属于Women类的instance: p1, 包含类中包含attribute: name, 我们把argument: "Mary" 给attribute name
p1.greeting()

p2 = greeting.Man("Leon")
print(p2.name)
p2.greeting()

x = y = z = 100
print(z)

b = 0.1
a = 0.2
print(round(a+b, 1))
"""
hello = "Hello"
"""
repeat_hello = hello*3
print(repeat_hello)
"""
hello = hello.upper()
print(hello)

quote = "He said: \nHello"
print(quote)

string1 = 'Python is fun!'
string2 = 'Let\'s learn it！'
string3 = string1 + ' ' + string2
print(string3)
a = 1
b = 2
print(a/b)

print(c_to_f(50))

x = 3
y = 5
less_than_result = x < y
print(less_than_result)

bool1 = True
bool2 = False
print(bool1<bool2)

print(compare(15, 12))

name = "Python"
print(check(name))
print(eligible_to_vote(89))

x = 10
y = 3
z = 8
result = (x>9 and y<5) and (x == 10 or y != 3)
print(result)
tester = all_over_zero(100, -1, 0)
print(tester)

words = ["a", "b", "c", "d"]
abcd = ''.join(words)
print(abcd)
#greeting_creater()

words = ["しの", "ちゃん", "が", "好きですが。", "自分のことのほうが大切だと思います。", "それで、自分のペースでも大丈夫です"]
sentence = "".join(words)
print(sentence)
#print(address_formatter())

text = "Python is fun!"
text_slicing = text[-3:]
print(text_slicing)

#extract_initials()
#reverse_words()
#print(palindrome_check())

"""
number = 0.88
formatted_number = f"The formatted number is {number:.2%}"
print(formatted_number)

text = "Hello"
formatted_text = f"string is: {text:>20}"
print(formatted_text)

personalized_greeting()

# 1. Define the data as a list of dictionaries
people = [
    {"name": "Alice", "age": '23', "city": "Tokyo"},
    {"name": "Bob", "age": '23', "city": "Osaka"},
    {"name": "Charlie", "age": '23', "city": "Kyoto"},
    {"name": "Diana", "age": '23', "city": "Fukuoka"},
]

# 2. Calculate the maximum width for each column to ensure alignment
# We check the length of the header and all data points in each column.
# We add 2 for extra padding.
name_width = max([len(p["name"]) for p in people] + [len("Name")]) + 2
age_width = max([len((p["age"])) for p in people] + [len("Age")]) + 2
city_width = max([len(p["city"]) for p in people] + [len("City")]) + 2

# 3. Print the table header
header = f"{'Name':<{name_width}}{'Age':<{age_width}}{'City':<{city_width}}"
print(header)

# 4. Print the separator line
separator = "=" * len(header)
print(separator)

# 5. Loop through the data and print each person as a formatted row
for person in people:
    row = f"{person['name']:<{name_width}}{person['age']:<{age_width}}{person['city']:<{city_width}}"
    print(row)
"""

'''
items_with_price = {'banane':'29', 'peach':'99', 'pear':'26', 'apple':'45'}#dictionary

def receipt_generator(items_with_price):
    The method aims to neatly generate the receipt of fruits
    fruit_length = max([len(f)for f in items_with_price]+[len('fruit')])+1#计算水果栏的宽度
    price_length = max([len(items_with_price[f])for f in items_with_price]+[len('price')])+1#计算价格栏的宽度

    header = f'{'Fruit':<{fruit_length}}{'Price':<{price_length}}'#定义表头,语法是：{'column_name':<{length}}, :<{length}代表以lenght进行左对齐
    print(header)

    for fruit in items_with_price:
        row = f"{fruit:<{fruit_length}}{items_with_price[fruit]:<{price_length}}"#每列都进行左对齐分别输出水果名(key)和对应的value
        print(row)

receipt_generator(items_with_price)
'''


#Generating personalized greeting
#name = input("Enter your name: ")#Accept the user's name which is inputed by user
#age = int(input("Enter your age: "))#Accept the age of user and transform it into int
#print("Hello, " + name + "! You are " + str(age) + " years old.")#take care of the rule in adding strings(transform age from int to str)

def area_of_reactangle(length, width):
    '''
    Args:
        arg1: length, this is the length of the ractangle
        arg2: width, this is the width of the ractange
    Return:
        By producting arg1 and arg2, the area of the rectangle would be returned.
    '''
    return length*width

x = 10 # set x to 10
y = 5  # set y to 5
z = x + y # add x and y, and give the result value to z
print(z) # print z
