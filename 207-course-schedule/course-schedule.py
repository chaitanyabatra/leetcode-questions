from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        directed graph

        if there is a cycle we have to return false else true

        we have edges and total courses[0...numcourses-1]->these are the nodes as a,b <=numcourses

        we'll make an adj using edges, 
        will make an indegree array to use kahn

        do toposort
        '''
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
        return len(topo)==numCourses
        