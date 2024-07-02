class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(numCourses)]
        for j,i in prerequisites:
            adj[i].append(j)
        indegree=[0 for _ in range(numCourses)]
        for i in range(numCourses):
            for a in adj[i]:
                indegree[a]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        topo=[]
        while q:
            node=q.popleft()
            topo.append(node)
            for a in adj[node]:
                indegree[a]-=1
                if indegree[a]==0:
                    q.append(a)
        return topo if len(topo)==numCourses else []