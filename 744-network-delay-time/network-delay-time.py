class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def djikstra(n,adj,k):
            pq=[]
            dist=[-1 for _ in range(n)]
            dist[k]=0
            heapq.heappush(pq,(0,k))
            while pq:
                d,node=heapq.heappop(pq)
                for a,e in adj[node]:
                    if dist[a]==-1 or dist[a]>d+e:
                        dist[a]=d+e
                        heapq.heappush(pq,(dist[a],a))
            return dist
        adj=[[] for _ in range(n)]
        for a,b,weight in times:
            adj[a-1].append((b-1,weight))
        dist=djikstra(n,adj,k-1)
        if -1 in dist:
            return -1
        return max(dist)