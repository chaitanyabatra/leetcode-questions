from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(node):
            i, j = node
            if vis[i][j]:
                return 0
            vis[i][j] = 1
         
            if board[i][j] == "E":
                # Directions for the 8 possible moves (left, right, up, down, and diagonals)
                dx=[]
                dy=[]
                for a in range(3):
                    for b in range(3):
                        if a!=1 or b!=1:
                            dx.append(a-1)
                            dy.append(b-1)
                adj=0
                for k in range(8):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny]=="M":adj+=1
                if adj == 0:
                    board[i][j] = "B"
                    for k in range(8):
                        nx=i+dx[k]
                        ny=j+dy[k]
                        if 0 <= nx < m and 0 <= ny < n:
                            dfs([nx, ny])
                else:
                    board[i][j] = str(adj)
            return 0
        
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            vis[i][j] = 1
            return board
        
        dfs(click)
        return board
