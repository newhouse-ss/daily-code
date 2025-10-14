import Area_rectangle_circle

def combined_area(length, height, radius):
    rec_area = Area_rectangle_circle.area_of_rectangle(length, height)
    cir_area = Area_rectangle_circle.area_of_circle(radius)
    return rec_area+cir_area

print(combined_area(5, 5, 1))