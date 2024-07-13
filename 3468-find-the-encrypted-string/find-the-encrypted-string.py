class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n=len(s)
        k=k%n
        s=s[k:]+s[:k]
        return s
        