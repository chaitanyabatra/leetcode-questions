class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            pick=nums[i-1]+dp[i-2] if i>1 else nums[i-1]
            not_pick=dp[i-1]
            dp[i]=max(pick,not_pick)
        return dp[n]

        