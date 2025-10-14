lst = [x for x in range(10)]
lst[-1:-1] = [x for x in range(10, 20, 2)]
print(lst)
lst.extend([x for x in range(10, 50, 10)])
print(lst)

full_list = [x for x in range(20)]
even_list = full_list[::2]
print(even_list)

even_odd = ['even' if x%2 == 0 else 'odd' for x in range(6)]
print(even_odd)