import random

level = input("please choose the difficulty: (H/E)")

while True:
    if level == 'H' or level == 'h':
        lower_bound = input("input lower bound: ")
        upper_bound = input("input upper bound: ")
        break
    elif level == 'E' or level == 'e':
        lower_bound = 1
        upper_bound = 100
        break
    else:
        print("please input \'H\' or \'E\'")
        continue

secret_number = random.randint(int(lower_bound), int(upper_bound))

count = 0
while True:
    if count>5:
        print('LOSE')
        again = input("Play again?(Y/N)")
        if again == 'Y':
            count = 0
            continue
        elif again == 'N':
            break
        else:
            print('invalid input!')

    guess = input("input a whole number here: ")
    count += 1
    try:
        guess_num = int(guess)
    except ValueError:
        print("please enter a whole number!")
        continue
    if guess_num>secret_number:
        print("Too large!")
    elif guess_num<secret_number:
        print("Too small!")
    else:
        print("Bingo!")
        break