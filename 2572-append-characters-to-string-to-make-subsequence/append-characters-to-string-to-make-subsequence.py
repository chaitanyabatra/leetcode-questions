class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j=0 
        i=0
        while j<len(t) and i<len(s):
            if s[i]==t[j]:
                j+=1
            i+=1

        return len(t)-j