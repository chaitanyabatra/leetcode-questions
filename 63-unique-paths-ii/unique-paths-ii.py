class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        #do init

        def f(i,j,dp):
            if obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            #base condn

            #memoise
            if dp[i][j]!=-1:return dp[i][j]
            
            dp[i][j]=f(i-1,j,dp)+f(i,j-1,dp)
            #formula
            return dp[i][j]
        return f(m-1,n-1,dp)


