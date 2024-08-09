# Transpose of a Matrix (easy)

# Write a Python function that computes the transpose of a given matrix.

def transpose(matrix):
    # Check if the input matrix is empty
    if not matrix:
        return []

    # Initialize the transposed matrix with the correct dimensions
    transposed = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    # Fill the transposed matrix by flipping rows and columns
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed[j][i] = matrix[i][j]

    return transposed

# Example usage
a = [[1, 2, 3], [4, 5, 6]]
output = transpose(a)
print(output)