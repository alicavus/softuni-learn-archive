# Exercise: Error Handling
# 4. Rotate Matrix

# Exceptions
class MatrixContentError(Exception):
    '''Raised when matrix contains any non numerical value'''
    pass

class MatrixSizeError(Exception):
    '''Raised when matrix is not a _perfect_ square''' # Nothing is ideally perfect, so stop being obsessive perfectionist
    pass

# Matrix rotation realisation
def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

mtrx = []

while True:
    line = input().split()

    if not line:
        break

    if not all(el.isdigit() for el in line):
        raise MatrixContentError("The matrix must consist of only integers")
    
    mtrx.append(line)

for row in mtrx:
    if len(mtrx) != len(row):
        raise MatrixSizeError("The size of the matrix is not a perfect square")

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')