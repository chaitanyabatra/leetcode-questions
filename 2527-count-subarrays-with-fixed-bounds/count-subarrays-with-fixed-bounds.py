class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxk: int) -> int:
        
        '''
        nums = [1,3,5,2,7,5], 
        minK = 1, 
        maxK = 5
        make different groups of array so you dont have to worry about numbers more and less than limit
        '''
        def solve(arr):
            n=len(arr)
            count=0
            lastmin,lastmax=-1,-1
            for i in range(n):
                if arr[i]==mink:
                    lastmin=i
                if arr[i]==maxk:
                    lastmax=i
                count+=min(lastmin,lastmax)+1
            return count




        arr=[]
        count=0
        for i in nums:
            if i>=mink and i<=maxk:
                arr.append(i)
            else:
                count+=solve(arr)
                arr=[]
        count+=solve(arr)
        return count