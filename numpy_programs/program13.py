# Create a checkerboard 8x8 matrix using the tile function 
import numpy as np
chess_board = np.tile( np.array([[1, 0],[0, 1]]), (4,4))
list1 = []
for array in chess_board:
    list1 = list(array)
    string = ' '.join(map(str, list1))
    print(string)