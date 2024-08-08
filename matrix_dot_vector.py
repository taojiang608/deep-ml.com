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