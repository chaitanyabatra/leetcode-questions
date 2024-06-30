class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def f(node):
            if not vis[node]:
                vis[node]=1
                for i in range(n):
                    if isConnected[node][i]:
                        f(i)
        n=len(isConnected)
        vis=[0]*n
        ans=0
        for i in range(n):
            if not vis[i]:
                ans+=1
                for j in range(n):
                    if isConnected[i][j]:
                        f(i)
        return ans