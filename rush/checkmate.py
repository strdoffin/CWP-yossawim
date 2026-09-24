def pawn(board,row,col):
    ap = [
        (-1,-1),
        (-1,1)
    ]
    for r, c in ap:
        sr = row + r
        sc = col + c
        if 0 <= sr < len(board) and 0 <= sc < len(board):
            if board[sr][sc] == "K":
                return True
    return False

def bishop(board,row,col):
    ap = [
        (-1,-1),
        (-1,1),
        (1,-1),
        (1,1)
    ]
    for r, c in ap:
        sr = row + r
        sc = col + c
        while 0 <= sr < len(board) and 0 <= sc < len(board):
            if board[sr][sc] == "K":
                return True
            if board[sr][sc] != ".":
                break
            sr += r
            sc += c
    return False

def rook(board,row,col):
    ap = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]
    for r, c in ap:
        sr = row + r
        sc = col + c
        while 0 <= sr < len(board) and 0 <= sc < len(board):
            if board[sr][sc] == "K":
                return True
            if board[sr][sc] != '.':
                break
            sr += r
            sc += c
    return False

def queen(board,row,col):
    return bishop(board,row,col) or rook(board,row,col)


def checkmate(board):
    board = board.splitlines()
    row = len(board)
    if row == 0:
        return "Error: Board not found!"

    for i in board:
        # print(len(i), row)
        if not (0 < row <= 8 and 0 < len(i) <= 8):
            return "Error: BoardSize incorrect!"
        if row != len(i):
            return "Error: Boardsize's Not SQUARE!"

    k_found = False
    for i in range(row):
        for j in range(row):
            if board[i][j] == 'K':
                if k_found:
                    return "Error: Found multiple KING."
                k_found = True
    if not k_found:
        return "Error: KING not found."
    for i in range(row):
        for j in range(row):
            o = board[i][j]
            if o == "P":
                if pawn(board,i,j):
                    return "Success"
            elif o == "B":
                if bishop(board,i,j):
                    return "Success"
            elif o == "R":
                if rook(board,i,j):
                    return "Success"
            elif o == "Q":
                if queen(board,i,j):
                    return "Success"
    return "Fail"