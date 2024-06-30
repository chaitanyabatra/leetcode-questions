from collections import deque
class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        old=grid[sr][sc]
        add[sr,sc] to q, do bfs where add dx,dx=[0,0,1,-1] to x,y(for i in range(4)) to get nx,ny
        if grid[nx][ny]==old:
            grid[nx][ny]=color
            q.append(nx,ny)
        '''
        old=grid[sr][sc]
        grid[sr][sc]=color
        if old==color:return grid
        q=deque()
        q.append([sr,sc])

        dx=[0,0,1,-1]
        dy=[1,-1,0,0]
        m,n=len(grid),len(grid[0])
        while q:
            node=q.popleft()
            x=node[0]
            y=node[1]
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx>=0 and ny>=0 and ny<n and nx<m and grid[nx][ny]==old:
                    grid[nx][ny]=color
                    print(nx,ny)
                    q.append([nx,ny])
        return grid