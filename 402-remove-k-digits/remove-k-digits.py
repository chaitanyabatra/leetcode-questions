class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for c in num:
            while len(stack) and k and stack[-1]>c:
                stack.pop()
                k-=1
            stack.append(c)
        
        while k and len(stack):
            stack.pop()
            k-=1


        r=''.join(stack).lstrip("0")
        if len(r)==0:return '0'
        return r

            
