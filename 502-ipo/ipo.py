class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        indices = set()
        for i in range(len(profits)):
            indices.add(i)
        curr_capital = w
        in_heap = set()
        projects = 0
        while projects < k:
            for idx in indices:
                if capital[idx] <= curr_capital:
                    heapq.heappush(max_heap, -profits[idx])
                    in_heap.add(idx)
            indices = indices - in_heap
            if not max_heap:
                return curr_capital
            curr_capital += -heapq.heappop(max_heap)
            projects += 1
        return curr_capital
