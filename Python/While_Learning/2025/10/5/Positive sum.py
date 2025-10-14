def posi_sum(list):
    total = 0
    for num in list:
        if num<=0:
            continue
        else:
            total+=num
    return total

list = [1,5,8,9,-4,-8,5,-2]
print(posi_sum(list))