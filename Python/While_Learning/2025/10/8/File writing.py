true_file = 'REAL.txt'
user_file = input("Please input the file you wnat to write: ")

def file_writing_validation(filename_u, filename_t):
    if filename_t == filename_u:
        try:
            with open(filename_u, 'w') as file:
                content = input("Write whatever you want: ")
                file.write(content)
        except IOError:
            print("The file is not writable.\nOr there's no space in memory.")

file_writing_validation(true_file, user_file)