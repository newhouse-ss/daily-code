file_name = input("Show me the filename.")
with open(file_name, 'a') as file:
    content = input("Now, write whatever you want, input: 'Done' to terminate.")
    while content != 'Done':
        file.write(content)
        content = input("Now, write whatever you want, input: 'Done' to terminate.")