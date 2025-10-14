def error_handling(height, length):
    if height < 0 or length < 0:
        return print('Invalid input.')
    else:
        return print(height*length)

error_handling(0, -2)