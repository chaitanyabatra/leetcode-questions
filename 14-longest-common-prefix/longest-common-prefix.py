class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=sorted(strs)
        ans=""
        a=s[0]
        b=s[-1]
        for i in range(min(len(a),len(b))):
            if s[0][i]!=s[-1][i]:
                return ans
            ans+=s[0][i]
        return ans