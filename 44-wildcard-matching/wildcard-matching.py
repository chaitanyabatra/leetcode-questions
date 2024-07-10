class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def isallstars(j):
            for i in range(j+1):
                if p[i]!="*":
                    return False
            return True
        def f(i,j):
            #base
            if i<0 and j<0:
                return True
            if i<0 and j>=0:
                return isallstars(j)
            if i>=0 and j<0:return False
            if dp[i][j]!=-1:return dp[i][j]

            #formula
            if s[i]==p[j] or p[j]=='?':
                dp[i][j]=f(i-1,j-1)
            elif p[j]=="*":
                dp[i][j]=f(i,j-1) or f(i-1,j)
            else:dp[i][j]=False
            return dp[i][j]
        m=len(s)
        n=len(p)
        dp=[[-1]*n for _ in range(m)]
        return f(m-1,n-1)
