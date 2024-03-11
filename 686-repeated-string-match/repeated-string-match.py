class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # #prefix
        # count=0
        # n=len(a)
        # for i in range(n):
        #     if a[i::]==b[:n-i+1]:
        #         #prefix true
        #         count+=1
        n=0
        aa=""
        while len(aa)<=(len(b)+2*len(a)):
            if b in aa:
                return n
            aa+=a
            n+=1
        return -1