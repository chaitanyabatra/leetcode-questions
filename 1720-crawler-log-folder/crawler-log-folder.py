class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if i=="./":
                continue
            elif i=="../":
                if stack:stack.pop()
            else:
                stack.append(i[:-1])
        return len(stack)