class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x = time//(n-1)
        y = time%(n-1)

        if y == 0: 
            return n if x%2!=0 else 1
        elif x%2 == 0: return 1+y
        else: return n-y