import numpy as np
rng = np.random.default_rng()
fruits = ['🍌', '🍎', '🍑', '🚗', '📷']
fruit = rng.choice(fruits, size = (3, 2))

print(np.random.uniform(low = 1, high = 10, size = (3, 2)))
print(fruit)