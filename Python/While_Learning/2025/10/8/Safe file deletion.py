import os

def safe_file_del(filename):
    try:
        with open(filename, 'r') as file:
            try:
                os.remove('numbers.txt')   
            except FileNotFoundError:
                print("No such file2.")
            except PermissionError:
                print("No permission to access.")
    except FileNotFoundError:
        print("No such file1.")

safe_file_del('numbers.txt')