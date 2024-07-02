class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        dp?
        start at opposite end, have outdegree 0s
        remove edges to it
        the nodes that become terminal are also safe, repeat this  until q empty, reverse kahn's
        """
        outdegree=[len(graph[i]) for i in range(len(graph))]
        revadj=[[]for _ in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[i]:
                revadj[j].append(i)
        q=deque()
        for i in range(len(graph)):
            if outdegree[i]==0:
                q.append(i)
        ans=set()
        while q:
            node=q.popleft()
            ans.add(node)
            for i in revadj[node]:
                outdegree[i]-=1
                if outdegree[i]==0:
                    q.append(i)
        return sorted(ans)
