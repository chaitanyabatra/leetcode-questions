class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(nums):
            n=len(nums)
            dp=[-1]*(n+1)
            dp[0]=0
            for i in range(1,n+1):
                pick= nums[i-1]+dp[i-2] if i>1 else nums[i-1]
                not_pick=dp[i-1]
                dp[i]=max(pick,not_pick)
                print(dp)
            return dp[n]
        return max(nums[0],f(nums[1:]),f(nums[:-1]))
        #nums[0] for the case of single element array