filename = "operate fiie"
file = open(filename, 'w')
file.write('Write something in Python script!\n')
file.write('And then print the content of the whole file.\n')
file.write('You could use file = open() merely to write something in file clearly.\n')
file.close()

try:
    with open(filename, 'r') as file:     
        content =   file.read()
        print(content)
except FileNotFoundError:
    print("No such file.")