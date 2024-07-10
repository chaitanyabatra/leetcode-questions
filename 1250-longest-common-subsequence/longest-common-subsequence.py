class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i1 in range(1,m+1):
            for i2 in range(1,n+1):

                if text1[i1-1]==text2[i2-1]:
                    dp[i1][i2]=1+dp[i1-1][i2-1]
                else:
                    dp[i1][i2]=max(dp[i1][i2-1],dp[i1-1][i2])

        return dp[m][n]