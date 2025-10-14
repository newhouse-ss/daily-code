import math

def distan_calcu(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

print(distan_calcu((1, 2), (3, 5)))