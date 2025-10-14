#Optimal:

def solve(col,board,ans,leftrow,upperdiagonal,lowerdiagonal,n):
    if col==n:
        ans.append(list(board))
        return

    for row in range(n):
        if (leftrow[row]==0
            and lowerdiagonal[row+col]==0
            and upperdiagonal[n-1+col-row]==0
        ):
            board [row]=board[row][:col]+"Q"+board[row][col+1:]
            leftrow[row]=1
            lowerdiagonal[row+col]=1
            upperdiagonal[]

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





