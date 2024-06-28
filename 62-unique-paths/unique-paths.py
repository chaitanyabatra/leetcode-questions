class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*m]*n
        for i in range(1,n):
            for j in range(1,m):
                #up and left
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[n-1][m-1]

        