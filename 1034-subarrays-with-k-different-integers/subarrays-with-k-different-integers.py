class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        

        def lt(k):
            l=0
            cnt=0
            distinct=0
            freq=[0]*20001
            n=len(nums)
            for r in range(n):
                a=nums[r]
                freq[a]+=1
                if freq[a]==1:distinct+=1
                while distinct>k:
                    b=nums[l]
                    freq[b]-=1
                    if freq[b]==0:distinct-=1
                    l+=1
                cnt+=(r-l+1)
            return cnt
        return lt(k)-lt(k-1)