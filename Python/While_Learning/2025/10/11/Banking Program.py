def show_balance():
    print(balance)

def deposit(in_num):
    global balance
    balance += int(in_num)

def withdraw(out_num):
    global balance
    if balance >= int(out_num):
        balance -= int(out_num)
    else:
        print("insufficient.")

balance = 0
sign = True

while sign:
    print("You could do the following things: ")
    print("1. Show the current balance of your account.")
    print("2. Deposit to your account.")
    print("3. Withdraw from your account.")
    print("4. Press Done if you want to execute.")
    mode = input("Input the number of thing you want to do: ")
    if mode == '1':
        show_balance()
    elif mode == '2':
        in_num = input("The number of money you want to deposit: ")#最好把这些描述写在函数中
        deposit(in_num)
    elif mode == '3':
        out_num = input("The number of money you want to withdraw: ")
        withdraw(out_num)
    elif mode == '4':
        sign = False
    else:
        print("Please input the valid number.")

        