file_name = input("Please give me the filename.")

with open(file_name, 'w') as file:
    given = input('write whatever you want: ')
    while given != 'Done':
        file.write(given)
        given = input('write whatever you want: ')