class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1 for i in range(len(graph))]

        for i in range(len(graph)):
            if color[i]!=-1:
                continue
            q=deque([[i,0]])
            while q:
                node,col=q.popleft()
                if color[node]==-1:
                    color[node]=col
                    for a in graph[node]:
                        q.append([a,col^1])
                if color[node]!=col:
                    return False
        return True

