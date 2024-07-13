class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        n=len(nums)
        dp=[[-1]*n for _ in range(n)]
        def f(i,j):
            #base case
            if i>j:return 0

            #memoise
            if dp[i][j]!=-1:return dp[i][j]

            ans=0
            for k in range(i,j+1):
                p1=f(i,k-1)
                p2=f(k+1,j)
                curr= nums[i-1]*nums[k]*nums[j+1]
                ans=max(ans,p1+p2+curr)
            dp[i][j]=ans
            return ans
        return f(1,len(nums)-2)
        