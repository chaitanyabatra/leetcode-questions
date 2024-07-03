class Solution:
    def minDifference(self, a: List[int]) -> int:

        
        if len(a)<=4:
            return 0
        a.sort()
        i=0
        mindif=a[-1]-a[0]
        for i in range(4):
            mindif=min(mindif,a[len(a)-4+i]-a[i])
        return mindif


        