import numpy as np
my_array = np.zeros((8, 8), dtype = int)
my_array[::2, 1::2] = 1
print(my_array)