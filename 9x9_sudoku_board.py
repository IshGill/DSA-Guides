def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    all_index_set = set()
    for rows in range(len(board)):
        for columns in range(len(board)):
            element = board[rows][columns]
            if element != ".":
                if (rows, element) in all_index_set or (element, columns) in all_index_set or (
                        rows // 3, columns // 3, element) in all_index_set:
                    return False
                else:
                    all_index_set.add((rows, element))
                    all_index_set.add((element, columns))
                    all_index_set.add((rows // 3, columns // 3, element))

    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
# Output: true