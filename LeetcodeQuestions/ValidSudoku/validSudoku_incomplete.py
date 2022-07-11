def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    #Each row must contain the digits 1-9 without repetition.
    for x in board:
        # i = 1
        # while i <= 9:
        #     if x.count(str(i)) <= 1:
        #         i += 1
        #     else:
        #         return False
        i = 0
        while i < 8:
            if x[i] != '.' and x[i] in x[i+1:]:
                return False
            i += 1



    # Each column must contain the digits 1-9 without repetition.
    # # flip
    # for r in range(9):
    #     for c in range(r):
    #         board[r][c], board[c][r] = board[c][r], board[r][c]
    # for x in board:
    #     i = 0
    #     while i < 9:
    #         if x[i] != '.' and x[i] in x[i+1:]:
    #             return False
    #         i += 1
    # #flip back
    # for r in range(9):
    #     for c in range(r):
    #         board[r][c], board[c][r] = board[c][r], board[r][c]

    c = 0
    while c < 9:
        temp = []
        for i in range(9):
            temp.append(board[i][c])
        r = 0
        while r < 8:
            if temp[r] != '.' and temp[r] in temp[r+1:]:
                return False
            r += 1
        c += 1



    # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    for r in range(3):
        c = 0
        while c < 3*r:
            board[r][c], board[c//3][3*r] = board[c//3][3*r], board[r][c]
            board[r][c+1], board[c//3][3*r+1] = board[c//3][3*r+1], board[r][c+1]
            board[r][c+2], board[c//3][3*r+2] = board[c//3][3*r+2], board[r][c+2]
            c += 3
    for r in range(3,6):
        c = 0
        while c < 3*(r-3):
            board[r][c] = board[c//3+3][3*(r-3)]
            board[r][c+1] = board[c//3+3][3*(r-3)+1]
            board[r][c+2] = board[c//3+3][3*(r-3)+2]
    for r in range(6,9):
        c = 0
        while c < 3*(r-6):
            board[r][c] = board[c//3+6][3*(r-6)]
            board[r][c+1] = board[c//3+6][3*(r-6)+1]
            board[r][c+2] = board[c//3+6][3*(r-6)+2]

    for x in board:
        i = 0
        while i < 8:
            if x[i] != '.' and x[i] in x[i+1:]:
                return False
            i += 1
    return True


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
