class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # #prefix
        # count=0
        # n=len(a)
        # for i in range(n):
        #     if a[i::]==b[:n-i+1]:
        #         #prefix true
        #         count+=1
        q=len(b)//len(a)
        r=len(b)%len(a)
        if r:
            q+=1
        if b in (a*q):
            return q
        elif b in (a*(q+1)):
            return (q+1)
        else:
            return -1