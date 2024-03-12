class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        while i<j:
            mid= i+(j-i)//2
            if mid&1:
                #make mid even
                mid-=1
            if nums[mid]!=nums[mid+1]:
                j=mid
            else:
                i=mid+2
        return nums[i]