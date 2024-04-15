# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self,root):
    
        ans=[]
        q=deque()
        q.append(root)
        if not root:
            return
        while q:
            if not q:
                return 
            level=[]
            n=len(q)
            for i in range(n):
                node=q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans