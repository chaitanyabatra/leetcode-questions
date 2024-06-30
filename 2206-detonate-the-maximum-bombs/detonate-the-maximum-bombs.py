from collections import deque
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        '''
        convert to directed edges(adj) list for each bomb at ith position in bombs as i
        N**2 time

        do bfs/dfs on each node and keep count of how many bombs are exploded
        N**2 time[N nodes se n-1 nodes max traverse]
        '''
        adj=[[] for _ in range(len(bombs))]
        for i in range(len(bombs)): #i is the exploding bomb
            for j in range(len(bombs)):
                if i!=j:
                    a=bombs[i]
                    b=bombs[j]
                    dx=abs(a[0]-b[0])
                    dy=abs(a[1]-b[1])
                    dist=(dx**2+dy**2)**(0.5)
                    if dist<=a[2]:
                        adj[i].append(j)
        max_bombs=1
        for i in range(len(bombs)):
            q=deque()
            q.append(i)
            exploded=[0 for _ in range(len(bombs))]
            exploded[i]=1
            while q:
                node=q.popleft()
                for i in adj[node]:
                    if exploded[i]==0:
                        exploded[i]=1
                        q.append(i)
            max_bombs=max(max_bombs,sum(exploded))
        return max_bombs

