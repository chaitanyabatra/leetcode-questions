class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        s=0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                s+=1
        return s