class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.


        start at corners, add corner Os to queue
        do bfs on queye, turn all Os and surrounding Os to "."

        traverse complete board, turn all Os to Xs, all "."s to Os
        """
        m,n=len(board),len(board[0])
        q=deque()
        for i in range(m):
            for j in range(n):
                if (i in [0,m-1] or j in [0,n-1]) and board[i][j]=='O':
                    board[i][j]="."
                    q.append([i,j])
        while q:
            i,j=q.popleft()
            dir=[(0,-1),(0,1),(1,0),(-1,0)]
            for dx,dy in dir:
                nx,ny =i+dx,j+dy
                if 0<=nx<m and 0<=ny<n and board[nx][ny]=="O":
                    board[nx][ny]="."
                    q.append([nx,ny])
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]==".":
                    board[i][j]="O"
        return board
