class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #check if sorted one side then perform normal binary search
        low=0
        high=len(nums)-1
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:return mid
            if nums[mid]>=nums[low]: #left side is sorted
                if nums[mid]>=target and nums[low]<=target:
                    high=mid-1
                else:
                    low=mid+1
            else: #riight side is sorted
                if nums[mid]<=target and nums[high]>=target:
                    low=mid+1
                else:
                    high=mid-1
        return -1