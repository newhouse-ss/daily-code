try:
    with open('application.log', 'x') as file:
        file.write("a new file.")
        message = input("The log message: ")
        timestamp = input("The time: ")
        file.write(message, timestamp)
except FileExistsError:
    print("already exists.")