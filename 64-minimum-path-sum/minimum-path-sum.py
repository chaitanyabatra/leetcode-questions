class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[-1 for _ in range(n)] for _ in range(m)]

        def f(m,n,dp):
            #basecase
            if m==0 and n==0:
                return grid[0][0]
            if m<0 or n<0:
                return math.inf
            #memoisation
            if dp[m][n]!=-1:return dp[m][n]
            #formula
            dp[m][n]=grid[m][n]+min(f(m-1,n,dp),f(m,n-1,dp))
            return dp[m][n]
        return f(m-1,n-1,dp)
        