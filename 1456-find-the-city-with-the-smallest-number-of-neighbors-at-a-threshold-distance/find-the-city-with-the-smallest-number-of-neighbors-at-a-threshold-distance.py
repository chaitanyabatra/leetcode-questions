class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix with infinity
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Fill the initial distances with the given edges
        for edge in edges:
            dist[edge[0]][edge[1]] = edge[2]
            dist[edge[1]][edge[0]] = edge[2]
        
        # Distance to self is always zero
        for i in range(n):
            dist[i][i] = 0
        
        # Floyd-Warshall algorithm to find the shortest paths between all pairs of cities
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Find the city with the smallest number of reachable cities within the distance threshold
        cntCity = n
        cityNo = -1
        for city in range(n):
            cnt = sum(1 for adjCity in range(n) if dist[city][adjCity] <= distanceThreshold)
            
            if cnt <= cntCity:
                cntCity = cnt
                cityNo = city
        
        return cityNo
