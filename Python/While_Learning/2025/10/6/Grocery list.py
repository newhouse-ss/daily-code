grocery_list = []
grocery_list.append('milk')
grocery_list.append('eggs')
grocery_list.append('bread')
grocery_list.insert(0, 'cheese')
grocery_list.append('sp')
grocery_list.remove("eggs")
grocery_list.sort(key = str.lower)
print(grocery_list)