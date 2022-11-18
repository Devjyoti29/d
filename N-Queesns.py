def NQueens(n,r,c):
    board=[[0 for i in range(n)] for j in range(n)]
    board[r][c]=1
    row=n

    def isSafe(board,r,c):
        #vertical
        i=r-1
        while(i>=0):
            if board[i][c]==1:
                return False
            i-=1
        i=r+1
        while(i<n):
            if board[i][c]==1:
                return False
            i+=1
        #left-diagonal
        i=r-1
        j=c-1
        while(i>=0 and j>=0):
            if board[i][j]==1:
                return False
            i-=1
            j-=1
        
        i=r+1
        j=c+1
        while(i<n and j<n):
            if board[i][j]==1:
                return False
            i+=1
            j+=1

        #right-diagonal
        i=r-1
        j=c+1
        while(j<row and i>=0):
            if board[i][j]==1:
                return False
            i-=1
            j+=1
        
        i=r+1
        j=c-1
        while(j>=0 and i<n):
            if board[i][j]==1:
                return False
            i+=1
            j-=1
        return True

            


    def printPath(r):
        if r==row:
            for i in range(n):
                for j in range(n):
                    print(board[i][j],end="")
                print()
            print()
            print()
            return
        for c in range(n):
            if board[r][c]==1:
                printPath(r+1)
            elif isSafe(board,r,c):
                board[r][c]=1
                printPath(r+1)
                board[r][c]=0
            
    printPath(0)

n=4
row=int(input("Enter row"))
col=int(input("Enter col"))
NQueens(n,row,col)