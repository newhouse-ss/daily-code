def read_chunk(file_name, chunk_size = 5):
    try:
        with open(file_name, 'r') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                print(chunk)
    except FileNotFoundError:
        print('No file.')
    except Exception:
        print("Others.")

read_chunk('peach.txt')