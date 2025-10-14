#1、定义需要的数据结构
#2、规划需要用到的函数：display answer，hint，print_mam
#写main函数，写其他函数

import random

answer_list = ["peach", "banana", "pear", "orange", "suika"]
hangman_stage = {0:("   ",
                    "   ",
                    "   "),
                 1:(" O ",
                    "   ",
                    "   "),
                 2:(" O ",
                    " | ",
                    "   "),
                 3:(" O ",
                    "/| ",
                    "   "),
                 4:(" O ",
                    "/|\\",
                    "   "),
                 5:(" O ",
                    "/|\\",
                    "/  "),
                 6:(" O ",
                    "/|\\",
                    "/ \\")}

def display_man(wrong_guess):
    for line in hangman_stage[wrong_guess]:
        print(line)

def display_hint(answer):
    mid = int(len(answer)/2)
    hint = answer[mid-1:mid+2]
    display1 = ["_" for i in range(mid-1)]
    display2 = ["_" for i in range(len(answer)-mid-2)]
    print(''.join(display1) + hint + ''.join(display2))

def display_answer(answer):
    print(answer)

def main():
    wrong_guess = 0 #Wrong guess times which corresponds to stage in hangman_stage
    answer = random.choice(answer_list)
    print("The game begins.")
    while wrong_guess < 6:
        hint = input("You can consume 1 chance to get some hint(Input Y/y to get hint): ")
        if hint.lower() == 'y':
            wrong_guess += 1
            display_hint(answer)
        if wrong_guess == 6:
            print("You dead.")
            display_answer(answer)
        guess = input("Now input your guess: ")
        if guess == answer:
            print("You survived")
            break
        else:
            print("Wrong guess! Be cautious, This is your status now:")
            wrong_guess += 1
            display_man(wrong_guess)
            chances = len(hangman_stage) - wrong_guess - 1
            print(f"Try again, after {chances} guess you will die.")
            continue

if __name__ == "__main__":
    main()