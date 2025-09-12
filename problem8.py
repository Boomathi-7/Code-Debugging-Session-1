# Problem8: Rotate a square matrix by 90 degrees clockwise.

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix.reverse()
    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
