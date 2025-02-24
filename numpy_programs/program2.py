import numpy as np
array1 = np.array([[1, 2], [3, 4]]) 
array2 = np.array([[1, 2], [3, 4]]) 

print(array1 == array2) 

comparison = (array1 == array2)
equal_arrays = comparison.all()

print(equal_arrays)
