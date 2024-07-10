class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def f(i,j):
            if j<0:return 1
            elif i<0: return 0

            if dp[i][j]!=-1:
                return dp[i][j]

            elif s[i]==t[j]:
                dp[i][j]= f(i-1,j)+f(i-1,j-1)
            else:
                dp[i][j]= f(i-1,j)
            return dp[i][j]
        m,n=len(s),len(t)
        dp=[[-1]*(n) for _ in range(m)]
        return f(m-1,n-1)