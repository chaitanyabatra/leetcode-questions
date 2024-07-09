class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
            cache={}
            def dfs(i,k): 
                if (i,k) in cache:
                    return cache[(i,k)]
                if i == len(nums):
                    if k == target:
                        cache[(i,k)]=1
                        return 1 
                    cache[(i,k)]=0
                    return 0 
                positive = dfs(i+1, k+ nums[i])
                negative = dfs(i+1, k - nums[i])
                cache[(i,k)]=positive + negative   
                return positive + negative     
            return dfs(0,0)


        