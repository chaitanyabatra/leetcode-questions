class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        map = {x : i for i, x in enumerate(arr2)}
        return sorted(arr1, key=lambda x: map[x] if x in map else 1001 + x)