class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(n,dp):
            if dp[n]!=-1:return dp[n]
            if n==0:
                return 0
            if n<0:
                return 0
            pick= nums[n-1]+f(n-2,dp)#n-1 in nums as it has 0 indexing while f has 1 indexing
            not_pick=f(n-1,dp)+0

            dp[n]=max(pick,not_pick)
            return dp[n]
        n=len(nums)
        dp=[-1]*(n+1)
        return f(n,dp)
