class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        ans=""
        a = sorted(freq, key=lambda x: freq[x], reverse=True)
        for i in a:
            ans+=i*freq[i]
        return ans

