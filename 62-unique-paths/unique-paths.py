class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def f(i,j,dp):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            #basecondn

            #memorization
            if dp[i][j]!=-1:return dp[i][j]

            #upandleft formula
            dp[i][j]=f(i,j-1,dp)+f(i-1,j,dp)

            print(dp)

            return dp[i][j]
        
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        return f(m-1,n-1,dp)

        