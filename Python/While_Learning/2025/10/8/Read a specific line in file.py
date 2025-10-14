def read_specific_line(file_name, asked_num):
    try:
        with open(file_name, 'r') as file:
            line_num = 0
            line = file.readline()
            while line:
                line_num += 1
                if line_num == asked_num:
                    print(line)
                line = file.readline()
    except FileNotFoundError:
        print('No file.')
    except Exception:
        print("X.")

read_specific_line('peach.txt', 3)