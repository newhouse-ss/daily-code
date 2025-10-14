def read_file(file_path):
    '''
    Opens a file and returns its content as a string.
    Handles FileNotFoundError gracefully.
    '''
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File open successfully!")
            return content
    except FileNotFoundError:
        print("No such file")
        return None
    except Exception as e:
        print(f"Something wrong happend: {e}")
        return None

def save_file(file_path, content):
    '''
    used to save the content inputed by user.
    argu: filename
    return: None
    '''
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return None
    except Exception as e:
        print(f'Something wrong: {e}')
        return None

def receive_input():
    '''
    Keep receiving strings given by user, store them in a list, 
    finally join and return them.
    '''
    input_str = input("Input what you want(Input \'Done\' if you want to stop): ")
    sentence_list = []
    while input_str != 'Done':
        sentence_list.append(input_str)
        input_str = input("Keep inputting(Input \'Done\' if you want to stop): ")
    return '\n'.join(sentence_list)

def main():
    filename = input("Input filename: ")
    action = input("Creating or Open a file?(c/o): ").lower()
    content = ''
    if action == 'o':
        content = read_file(filename)
        print(content)
        if not content:
            print("Starting with an empty file.")
            content = ''
    elif action == 'c':
        print("Creating a file.")
    else:
        print("Wrong input!")
        return
    content += receive_input()
    save = input("Save or not? \'s\' to save, \'n\' to keep: ").lower()
    if save  == 's':
        save_file(filename, content)
    else:
        print("Changes no saved.")

if __name__ == '__main__':
    main()