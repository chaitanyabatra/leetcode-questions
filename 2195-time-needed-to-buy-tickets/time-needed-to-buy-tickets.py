class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count=0
        for i in range(k+1):
            if tickets[i]<=tickets[k]:
                count+=tickets[i]
            else:
                count+=tickets[k]
        for i in range(k+1,len(tickets)):
            if tickets[i]<tickets[k]:
                count+=tickets[i]
            else:
                count+=(tickets[k]-1)
        return count
            