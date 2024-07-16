class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        r=s[::-1]
        @lru_cache
        def f(i1,i2):
            if i1<0 or i2<0:return 0
            if dp[i1][i2]!=-1:return dp[i1][i2]
            if s[i1]==r[i2]:
                dp[i1][i2]=1+f(i1-1,i2-1)
            else:
                dp[i1][i2]=max(f(i1,i2-1),f(i1-1,i2))
            return dp[i1][i2]
        m=len(s)
        n=len(r)
        dp=[[-1]*n for _ in range(m)]
        return f(m-1,n-1)
        