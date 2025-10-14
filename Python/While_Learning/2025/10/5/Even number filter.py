def even_num_filter(list):
    for num in list:
        if num == 10:
            break
        if num%2 == 1:
            print(num)
        else:
            print("even")

even_num_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])