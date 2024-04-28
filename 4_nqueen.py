def is_safe(board,row,col,n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
        
    for i,j in zip(range(row,n,1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    return True

def backtracking_util(board,col,n):
    if col >= n:
        return True
    
    for i in range(n):
        if is_safe(board,i,col,n):
            board[i][col] = 1
            if backtracking_util(board,col+1,n):
                return True
            board[i][col] = 0
    return False

def bractracking(n):
    board = [[0] * n for i in range(n)]

    if not backtracking_util(board,0,n):
        print("Solution does not exist")
    else:
        print("Solution using backtracking: ")
        for row in board:
            print("".join('Q ' if x==1 else '. ' for x in row))


def under_attack(board, row, col, n):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return True
    return False


def branch_n_bound_util(board, row, n):
    if row == n:
        return True
    
    for col in range(n):
        if not under_attack(board, row, col, n):
            board[row] = col
            if branch_n_bound_util(board, row + 1, n):
                return True
            board[row] = 0
    return False

def branch_n_bound(n):
    board = [0] * n 

    if not branch_n_bound_util(board,0,n):
        print("Solution does not exist")
    else:
        print("Solution using branch and bound: ")
        for row in board:
            print("".join("Q " if x == row else ". " for x in range(n)))


n = int(input("Enter size of chessboard: "))
bractracking(n)
branch_n_bound(n)