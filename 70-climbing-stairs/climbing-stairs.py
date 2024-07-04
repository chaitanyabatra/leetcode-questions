class Solution:
    def climbStairs(self, n: int) -> int:
        if n<4:return n
        one=1
        two=2
        three=0
        for i in range(2,n):
            three=one+two
            one=two
            two=three
        return two