def symmetric_difference_of_nums(set_1, set_2):
    return set_1.symmetric_difference(set_2)
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}

print(symmetric_difference_of_nums(set_1, set_2))
set_1.remove(6)