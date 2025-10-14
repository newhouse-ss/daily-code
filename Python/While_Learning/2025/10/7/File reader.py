file_name = input('Please input the file name: ')
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('File not found.')