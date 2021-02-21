def rotateMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    [matrix[i].reverse() for i in range(len(matrix))]

    return matrix
print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))