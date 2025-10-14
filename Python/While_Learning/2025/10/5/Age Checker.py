#Age Checker
def age_checker(age):
    '''
    arg: The age inputed by the user
    return: According to the age of user, print the status of him/her.
    '''
    if int(age) < 13:
        print("You are a child.")
    elif int(age) < 19:
        print("You are a teenager.")
    else:
        print("You are an adult.")

user_age = input("Please input you age: ")
age_checker(user_age)



'''
username = input("Enter your username: ")
if username == "":
    print("Username cannot be empty.")
else:
    print("Username is valid.")

password = input("Enter your password: ")
if len(password) < 8:
    print("Password must be at least 8 characters long.")
else:
    print("Password is valid.")
'''
