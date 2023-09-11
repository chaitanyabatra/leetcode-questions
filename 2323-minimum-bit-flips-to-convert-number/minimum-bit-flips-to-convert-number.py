class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0
        while start or goal:
            a=start&1
            b=goal&1
            count+=a^b
            start>>=1
            goal>>=1
        return count
        