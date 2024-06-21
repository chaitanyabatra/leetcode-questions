class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Calculate initial satisfaction without using the technique
        initial_satisfaction = 0
        for i in range(n):
            if grumpy[i] == 0:
                initial_satisfaction += customers[i]
        
        # Calculate the additional satisfaction using the technique
        max_additional_satisfaction = 0
        current_additional_satisfaction = 0
        
        # First window
        for i in range(minutes):
            if grumpy[i] == 1:
                current_additional_satisfaction += customers[i]
        
        max_additional_satisfaction = current_additional_satisfaction
        
        # Slide the window from start to end of the array
        for i in range(minutes, n):
            if grumpy[i] == 1:
                current_additional_satisfaction += customers[i]
            if grumpy[i - minutes] == 1:
                current_additional_satisfaction -= customers[i - minutes]
            
            max_additional_satisfaction = max(max_additional_satisfaction, current_additional_satisfaction)
        
        return initial_satisfaction + max_additional_satisfaction