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