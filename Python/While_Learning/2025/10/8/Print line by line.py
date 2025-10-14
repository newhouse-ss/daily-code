def print_line_by_line(name):
    with open(name, 'r') as file:
        for line in file:
            print(line)

print_line_by_line('peach.txt')

def print_chunk(file_name):
    try:
        with open(file_name, 'r') as file:
            chunk1 = file.read(10)
            print(f"Chunk1 contains: {chunk1}")
    except FileNotFoundError:
        print("No such file.")
    except Exception:
        print("Something unknown happens...")

print(print_chunk('peach.txt'))