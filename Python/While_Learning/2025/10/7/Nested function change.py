def grandparent():
    local_var = 0
    def parent():
        nonlocal local_var
        local_var += 8
    def child():
        nonlocal local_var
        a = local_var
        return a
    parent()
    return child()

print(grandparent())