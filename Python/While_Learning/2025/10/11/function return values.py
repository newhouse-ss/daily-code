def area_and_perimeter(width, height):
    area = width * height
    perimeter = (width + height) * 2
    return area, perimeter

area, perimeter = area_and_perimeter(2, 3)
print(area)
print(perimeter)