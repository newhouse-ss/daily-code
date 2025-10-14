def user_input():
    file_name = input('Please input the filename: ')
    try:
        with open(file_name, 'w') as file:
            user_in = input("Input whatever you want(Press Done to terminate): ")
            while user_in != 'Done':
                file.write(user_in+'\n')
                user_in = input('Keep writing: ')
    except Exception:
        print("Unknown error.")

user_input()