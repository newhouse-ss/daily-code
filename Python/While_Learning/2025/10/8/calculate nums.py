def nums_calculator(num_file):
    try:
        total = 0
        with open(num_file,'r') as file:
            for line in file:
                try:
                    number  = int(line.strip())
                    total += number
                except ValueError:
                    print(f"This line is not a number: {line}")
        return print(total)
    except FileNotFoundError:
        print("No such file.")
        return None

nums_calculator('numbers.txt')