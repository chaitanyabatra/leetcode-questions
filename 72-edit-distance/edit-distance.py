class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def f(i,j):
            if i<0 or j<0:return max(i+1,j+1)

            if dp[i][j]!=-1:return dp[i][j]

            if word1[i]==word2[j]:
                dp[i][j]=f(i-1,j-1)+0
                return dp[i][j]
            else:
                dp[i][j]=1+min(
                    f(i-1,j-1),
                    min(f(i-1,j),f(i,j-1))
                )
                return dp[i][j]
        m,n=len(word1),len(word2)
        dp=[[-1]*(n) for _ in range(m)]
        return f(m-1,n-1)
         
        