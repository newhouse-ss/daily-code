def add_num_series(N):
    total = 0
    for i in range(1, N+1):
        if i%5 == 0 or i%7 == 0:
            continue
        total += i
    return total

print(add_num_series(10))