class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        prefix=[0]*n
        suffix=[0]*n
        maxprefix=0
        for i in range(n):
            prefix[i]=max(maxprefix,height[i])
            maxprefix=prefix[i]
        maxsuffix=0
        for i in range(n-1,-1,-1):
            suffix[i]=max(maxsuffix,height[i])
            maxsuffix=suffix[i]
        water=[0]*n
        for i in range(n):
            water[i]=min(prefix[i],suffix[i])
            water[i]-=height[i]
        print(water)
        return sum(water)

        