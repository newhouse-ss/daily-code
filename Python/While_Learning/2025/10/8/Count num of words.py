def words_counter(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            content_list = content.split()
            print(content_list)
            print(len(content_list))
    except FileNotFoundError:
        print("No such file.")
    except Exception:
        print("Unknown error happens.")

input_file = 'peach.txt'
words_counter(input_file)