import random

def slot_row(symbol_list):
    result_list = [random.choice(symbol_list) for symbol in range(3)]
    return result_list

def print_row(result_list):
    print(' | '.join(result_list))

def calculate_money(bet):
    return 10*bet

def main():
    balance = 100
    sign = True

    print("Welcome to the slot machine game!")
    print("These are possible symbols in the game: ")
    symbol_list = ['🍏', '🍑', '🍋', '🟠', '❤️ ']
    print(' | '.join(symbol_list))

    while balance > 0:
        
        bet = input("Input the number of money you want to bet(press Done to finish): ")
        if bet == 'Done':
            print(f'You balance is: {balance}')
            print("Thank you!")
            break
        if not bet.isdigit():
            print("You need to input a positive number.")
            continue

        bet = int(bet)
        if bet > balance:
            print("The balance is insufficient!")
            continue
        elif bet == 0:#不用小于零，因为小于零的东西不会过isdigit()
            print("You need to input a positive number.")
            continue
        balance -= bet
        print(f"The current balance: {balance}")
        result_list = slot_row(symbol_list)
        print_row(result_list)

        if result_list[0] == result_list[1] == result_list[2]:
            win = calculate_money(bet)
            balance += win
            print(f'You win: {win}, now your balance is: {balance}')
    print("Finished.")
if __name__ == '__main__':
    main()