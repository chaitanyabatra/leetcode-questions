from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        count total number of oranges, add all rotten x,y in a queue
        made dx dy as -1 1 0 0
        did bfs on queue, for each 2, turnt their neighbouring 1s to 2 and added to queue if q still there add 1 to day
        '''
        m=len(grid)
        n=len(grid[0])
        total=0#total rotten
        days=0
        count=0#count rotten
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:total+=1
                if grid[i][j]==2:q.append([i,j])
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]
        if not q and not total:return 0
        while q:
            k=len(q)
            count+=k
            while k:
                k-=1
                node=q.popleft()
                x=node[0]
                y=node[1]
                for i in range(4):
                    xx=x+dx[i]
                    yy=y+dy[i]
                    if xx>=0 and yy>=0 and xx<m and yy<n and grid[xx][yy]==1:
                        q.append([xx,yy])
                        grid[xx][yy]=2
            days+=1
        if total==count:return days-1
        return -1


        
