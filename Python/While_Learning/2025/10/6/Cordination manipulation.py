def mid_point(tuple1, tuple2):
    avg_x = (tuple1[0]+tuple2[0])/2
    avg_y = (tuple1[1]+tuple2[1])/2
    return avg_x, avg_y
tp1 = (1, 3)
tp2 = (2, 8)
c = mid_point(tp1, tp2)
print(c)
print(type(c))