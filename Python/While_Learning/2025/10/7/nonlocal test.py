def counter():
    counter = 0
    def increment():
        nonlocal counter
        counter += 1
        return counter
    return increment

a = counter()#a接受的值是increment这个函数，所以在后续的调用a()时，counter函数始终没有结束因此counter的值可以累计
print(a())
print(a())
print(a())
def counter():
    count = 0 # This is enclosed in counter

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

# Create an instance of the counter
my_counter = counter()

# Call the increment function multiple times
print(my_counter()) # Output: 1
print(my_counter()) # Output: 2
print(my_counter()) # Output: 3