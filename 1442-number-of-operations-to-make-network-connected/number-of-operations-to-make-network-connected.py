class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1: return -1

        parent = [i for i in range(n)]
        size = [1] * (n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2: return

            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1]+=size[p2]
            else:
                parent[p1]=p2
                size[p2]+=size[p1]
        
        unconnected = n-1
        for a,b in connections:
            if find(a) == find(b): continue
            unconnected -= 1
            union(a, b)

        return unconnected