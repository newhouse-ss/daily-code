import random

seed = random.seed(43)

print(random.random())
print(random.randint(1, 20))

seed = random.seed(42)

print(random.random())
print(random.randint(1, 20))