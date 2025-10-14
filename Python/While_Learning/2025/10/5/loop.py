def list_iteration(List):
    for item in List:
        print(item)

def gusser():
    answer = '9'
    num = input("Input your guess: ")
    while num!=answer:
        print('WRONG!')
        num = input("Input your guess: ")
    print("BINGO!")

lst = ["Introduction to Algorithm", "Deep Learning", "L'Étranger"]
list_iteration(lst)
string1 = "shino"
list_iteration(string1)

gusser()

while True:
    user_input = input("please input a number(or press \'q\'to quit.): ")

    if user_input.lower() == 'q':
        break

    try:
        num = float(user_input)
        print(f'You entered {num}')
    except ValueError:
        print("Value error")
        continue

