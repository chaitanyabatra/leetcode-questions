class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        def f(ind,buy):
            if ind==n:
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy==0:
                op1=0+f(ind+1,0)
                op2=-prices[ind]+f(ind+1,1)
            if buy==1:
                op1=0+f(ind+1,1)
                op2=prices[ind]+f(ind+1,0)
            dp[ind][buy]= max(op1,op2)
            return dp[ind][buy]
        
        return f(0,0)

        