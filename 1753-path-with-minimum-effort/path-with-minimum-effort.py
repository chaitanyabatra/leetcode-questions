import heapq as hq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        make dist 2d and heapq
        dist[0][0]=1
        push diff,i,j to heap for start
        make dir 0,0,1-1
        while heap:
            d,i,j=pop
            #basecond
            if i==m-1 and j==n-1:return d
            loop over dir:
            nx ny
            if in boundary, update max d
            if dist[nx][ny]>d: update dist and push to queue


        '''
        m,n=len(heights),len(heights[0])
        dist=[[-1 for _ in range(n)] for _ in range(m)]
        pq=[]
        dist[0][0]=0
        hq.heappush(pq,(0,0,0))
        dir=[(-1,0),(0,-1),(0,1),(1,0)]
        while pq:
            d,i,j=hq.heappop(pq)
            if i==m-1 and j==n-1:
                return d
            for dx,dy in dir:
                nx,ny=i+dx,j+dy
                if 0<=nx<m and 0<=ny<n :
                    nd=max(d,abs(heights[i][j]-heights[nx][ny]))
                    if dist[nx][ny]==-1 or dist[nx][ny]>nd:
                        dist[nx][ny]=nd
                        hq.heappush(pq,(dist[nx][ny],nx,ny))
        return 0



        