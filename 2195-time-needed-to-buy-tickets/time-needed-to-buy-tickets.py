class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count=0
        for i in range(k+1):
            count+=min(tickets[i],tickets[k])
        for i in range(k+1,len(tickets)):
            count+=min(tickets[i],tickets[k]-1)
        return count
            