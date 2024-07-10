class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)
        dp=[[[-1]*3 for _ in range(2)] for _ in range(n)]
        def f(ind,buy,cap):
            if ind==n:
                return 0
            if dp[ind][buy][cap]!=-1:
                return dp[ind][buy][cap]
            if cap==0:
                if buy==1:
                    op1=prices[ind]+f(ind+1,0,cap)#sell
                    op2=f(ind+1,1,cap)#notsell
                else:
                    return 0
            else:
                if buy==0:
                    op1=0+f(ind+1,0,cap)#notbuy
                    op2=-prices[ind]+f(ind+1,1,cap-1)#buy
                if buy==1:
                    op1=0+f(ind+1,1,cap)#notsell
                    op2=prices[ind]+f(ind+1,0,cap)#sell
            dp[ind][buy][cap]= max(op1,op2)
            return dp[ind][buy][cap]
        
        return f(0,0,2)
        