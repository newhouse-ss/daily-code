try:
    with open("numpy.txt", 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('Error')