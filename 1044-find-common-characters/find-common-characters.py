class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = Counter(words[0])
        for word in words:
            min_freq &= Counter(word)
        print(min_freq)
        return list(min_freq.elements())