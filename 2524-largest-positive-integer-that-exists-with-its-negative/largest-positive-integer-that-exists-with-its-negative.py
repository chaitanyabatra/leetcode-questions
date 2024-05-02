class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums=sorted(nums)
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]==-1*nums[j]:
                break
            elif -1*nums[i]<=nums[j]:
                j-=1
            else:
                i+=1
        return nums[j] if nums[i]==-1*nums[j] else -1