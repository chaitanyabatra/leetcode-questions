class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count=0
        while numBottles>=numExchange:
            numBottles-=numExchange
            count+=numExchange
            numBottles+=1
        count+=numBottles
        return count