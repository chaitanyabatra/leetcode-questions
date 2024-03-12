class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j=len(needle)
        for i in range(len(haystack)):
            if needle==haystack[i:i+j]:return i
        return -1