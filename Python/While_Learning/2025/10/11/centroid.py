tps = [(1, 2), (3, 4), (5, 6)]

def calcu_centroid(list_of_tps):
    sum_x = sum_y = 0
    for tp in list_of_tps:
        sum_x += tp[0]
    for tp in list_of_tps:
        sum_y += tp[1]
    length = len(list_of_tps)

    return (sum_x/length, sum_y/length)

print(calcu_centroid(tps))