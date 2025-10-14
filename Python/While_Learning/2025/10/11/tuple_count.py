tp = (1, 2, 3, 4, 5, 5, 4)
print(tp.count(5))

try:
    print(tp.index(8, 4, 5))
except ValueError:
    print("The number could not be found in the given realm.")    