class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        dp[0]=0
        dp[1]=nums[0]
        #dp[2]=max(dp[1],nums[1])
        for i in range(2,n+1):
            a,b,c=0,0,0
            a=dp[i-1]
            if i>1:b=dp[i-2]+nums[i-1]
            if i>2:c=dp[i-3]+nums[i-1]
            dp[i]=max(a,b,c)
            print(dp)
        return dp[n]
