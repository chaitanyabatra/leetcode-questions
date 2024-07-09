class Solution:
    #def coinChange(self, coins: List[int], amount: int) -> int:
        #pick not pick starting from big to small
        #recursion
        #base case- amount==0
        #parameters, index and amount, returns min number of coins needed
        #pick=amount//coins[i]+f(i-1,amount-coins[i](amount//coins[i])) if coins[i]<amount else inf
        #notpick=f(i-1,amount)
    def coinChange(self,coins, amount):
        memo = [-2] * (amount + 1)
        def helper(amount):
            if amount == 0: return 0
            if amount < 0: return -1
            if memo[amount] != -2: return memo[amount]
            minCoins = float('inf')
            for coin in coins:
                res = helper(amount - coin)
                if res >= 0: 
                    minCoins = min(minCoins, 1 + res)
            memo[amount] = minCoins if minCoins != float('inf') else -1
            return memo[amount]
        return helper(amount)