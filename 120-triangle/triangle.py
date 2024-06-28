class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[]
        for i in range(1,n+1):
            dp.append([-1 for _ in range(i)])
        dp[0][0]=triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                #basecase
                if j==0:
                    dp[i][j]=triangle[i][j]+dp[i-1][j]
                elif j==i:
                    dp[i][j]=triangle[i][j]+dp[i-1][j-1]
                else:
                    dp[i][j]=triangle[i][j]+min(dp[i-1][j],dp[i-1][j-1])
        return min(dp[-1])
        