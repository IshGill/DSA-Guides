def zeroMatrix(matrix):
    column, row = set(), set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                column.add(j), row.add(i)

    for i in column:
        for k in range(len(matrix)):
            matrix[k][i] = 0

    for i in row:
        for k in range(len(matrix)):
            matrix[i][k] = 0

    return matrix


print(zeroMatrix([[1,1,1],[1,0,1],[1,1,1]]))