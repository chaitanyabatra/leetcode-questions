class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        targ=sum(nums)//2
        if sum(nums)&1:return False
        n=len(nums)
        dp=[[-1]*(targ+1) for _ in range(n)]
        def f(i,target,dp):
            if dp[i][target]!=-1:return dp[i][target]
            if target==0:return True
            if i==0:return nums[i]==target
            if i<0:return False
            
            not_take = f(i - 1, target,dp)
            # Include the current element (only if it's not greater than the remaining target)
            take = False
            if nums[i] <= target:
                take = f(i - 1, target - nums[i],dp)
            
            # Memoize the result
            dp[i][target] = take or not_take
            return dp[i][target]

        return f(n-1,targ,dp)