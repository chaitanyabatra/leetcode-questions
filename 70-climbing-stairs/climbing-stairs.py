class Solution:
    def climbStairs(self,n):
        dp=[-1]*(n+1)
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
            print(dp)
        return dp[n]
