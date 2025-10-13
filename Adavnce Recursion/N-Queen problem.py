#Brute Force:

def solve(col,board,ans,n):
    if col==n:
        ans.append(list(board))
        return

    for row in range(n):
        if isSafe(row,col,board,n):
            board[row]=board[row][:col]+"Q"+board[row][col+1:]
            solve(col+1,board,ans,n)
            board[row]=board[row][:col]+"."+board[row][col+1:]

def isSafe(row,col,board,n):
    dup_row=row
    dup_col=col

    while row>=0 and col>=0:
        if board[row][col]=="Q":
            return False
        row-=1
        col-=1
    col=dup_col
    row=dup_row

    while col>=0:
        if board[row][col]=="Q":
            return False
        col-=1

    row=dup_row
    col=dup_col

    while row<n and col>=0:
        if board[row][col]=="Q":
            return False
        row+=1
        col-=1

    return True

def solveNQueens(n):
    board = ["." * n for _ in range(n)]  # initialize board
    ans = []
    solve(0, board, ans, n)
    return ans

n=int(input("Enter a number :"))
print(solveNQueens(n))





