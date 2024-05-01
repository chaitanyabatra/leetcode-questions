class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index=0
        for i in range(len(word)):
            if word[i]==ch:
                index=i
                break
        word=word[:index+1][::-1]+word[index+1:]
        return word