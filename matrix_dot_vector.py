# 1. Matrix times Vector (easy)

# Write a Python function that takes the dot product of a matrix and a vector. 
# return -1 if the matrix could not be dotted with the vector

import numpy as np

def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    # Convert inputs to numpy arrays
    a = np.array(a)
    b = np.array(b)
    
    # Check if the number of columns in the matrix equals the number of elements in the vector
    if a.shape[1] != b.shape[0]:
        return -1
    
    # Calculate the dot product
    c = np.dot(a, b)
    
    return c


def matrix_dot_vector(matrix, vector):
    # Check if the number of columns in the matrix equals the number of elements in the vector
    if len(matrix[0]) != len(vector):
        return -1
    
    # Initialize the result list
    result = []
    
    # Compute the dot product
    for row in matrix:
        dot_product_value = 0
        for i in range(len(row)):
            dot_product_value += row[i] * vector[i]
        result.append(dot_product_value)
    
    return result

# Example usage
matrix = [[1, 2, 3], [4, 5, 6]]
vector = [7, 8, 9]

result = matrix_dot_vector(matrix, vector)
print(result)  # Output: [50, 122]

# Example with incompatible dimensions
matrix2 = [[1, 2], [3, 4], [5, 6]]
vector2 = [7, 8, 9]
result2 = matrix_dot_vector(matrix2, vector2)
print(result2)  # Output: -1
