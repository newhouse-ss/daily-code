import time

start_time = time.time()
lst = []
for i in range(1000000):
    lst.append([i, i])
end_time = time.time()
cost_l = end_time - start_time

start_time = time.time()
lst_tuple = []
for i in range(1000000):
    lst_tuple.append((i, i))
end_time = time.time()
cost_t = end_time - start_time

print(f"Cost of list: {cost_l}")
print(f"Cost of tuple: {cost_t}")