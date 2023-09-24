class Solution:
    @staticmethod
    def cmp(s1, s2):
        return len(s1) < len(s2)
    def longestStrChain(self, words):
        words.sort(key=lambda x: len(x))
        ump = {}
        ans = 0

        for w in words:
            longest = 0
            for i in range(len(w)):
                sub = w[:i] + w[i + 1:]
                longest = max(longest, ump.get(sub, 0) + 1)

            ump[w] = longest
            ans = max(ans, longest)

        return ans
