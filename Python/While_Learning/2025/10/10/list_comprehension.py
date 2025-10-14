a = [1, 2, 3, 4, 5]

a[:] = [x**2 if x%2 == 0 else x for x in a]
print(a)

a.extend([5, 8, 9])
print(a)

del a[2:4]
print(a)

print(a.pop())

a.remove(5)
print(a)

a.insert(0, 5)
print(a)

inventory = ["a", 'b', 'c']
inventory.extend(['d', 'e'])
inventory.remove('e')
print(inventory)

celsius_temperatures = [0, 10, 22.5, 30, 100]
convert = [(c*9/5)+32 for c in celsius_temperatures]
print(convert)