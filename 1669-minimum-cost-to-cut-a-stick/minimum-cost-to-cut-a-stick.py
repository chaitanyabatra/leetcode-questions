class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(n)
        cuts.append(0)
        cuts.sort()

        dp=[[-1]*(len(cuts))for _ in range(len(cuts))]
        def f(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:return dp[i][j]
            mini=float('inf')
            for k in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1]+f(i,k-1)+f(k+1,j)
                mini=min(mini,cost)
            dp[i][j]= mini
            return mini
        return f(1,len(cuts)-2)
        