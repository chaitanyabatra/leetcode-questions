class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1]*2 for _ in range(2)] for _ in range(n)]
        def f(ind,buy,cooldown):

            if ind==n:
                return 0
            if dp[ind][buy][cooldown]!=-1:
                return dp[ind][buy][cooldown]
            if cooldown==1:
                return 0+ f(ind+1,buy,0)
            if buy==0:
                op1=0+f(ind+1,0,0)#notbuy
                op2=-prices[ind]+f(ind+1,1,0)#buy
            if buy==1:
                op1=0+f(ind+1,1,0)#notsell
                op2=prices[ind]+f(ind+1,0,1)#sell
            dp[ind][buy][cooldown]= max(op1,op2)
            return dp[ind][buy][cooldown]
        
        return f(0,0,0)