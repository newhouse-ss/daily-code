def nested_loop_break():
    for i in range(1, 6):
        print(f"outer:{i}")
        for j in range(1, 6):
            print(f"inner:{j}")
            if i*j>12:
                break
nested_loop_break()
