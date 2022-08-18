import numpy as np

matrix = np.array([[1, 2, 0], [2, 1, 0], [4, -1, 0]])

inv_matrix = np.linalg.inv(matrix)
print(inv_matrix)
