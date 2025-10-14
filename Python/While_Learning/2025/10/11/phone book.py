pb = {
    "father":111,
    "mother":222,
    "brother":222
}
mode = input("Input the mode you want to do(add, del, change, search): ")

if mode == 'add':
    name = input("Input the name of him/her: ")
    num = input("num of her.")
    pb[name] = num
elif mode == 'del':
    name = input("Input the person you want to delete: ")
    del pb[name]
elif mode == 'change':
    name = input("name: ")
    updated = input("number: ")
    pb[name] = updated
elif mode == 'search':
    name = input("Search name: ")
    print(pb[name])
else:
    print("Invalid input.")