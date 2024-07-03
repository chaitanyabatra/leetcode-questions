from collections import deque
from typing import List, Tuple

class Solution:
    def findCheapestPrice(self, n: int, flights: List[Tuple[int, int, int]], src: int, dst: int, bruh: int) -> int:
        # Create adjacency list
        adj=[[] for _ in range(n)]
        for i,j,k in flights:
            adj[i].append((j,k))
        print(adj)
        dist=[-1 for _ in range(n)]
        dist[src]=0
        q=deque()
        q.append([0,src,0])
        while q:
            snd=q.popleft()
            s,n,d=snd
            if s>bruh:continue
            for ae in adj[n]:
                a,e =ae
                if (dist[a]==-1 or dist[a]>d+e):
                    dist[a]=d+e
                    q.append([s+1,a,d+e])
            print(dist)
        return dist[dst]
