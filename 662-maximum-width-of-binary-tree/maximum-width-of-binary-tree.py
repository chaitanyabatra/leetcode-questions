# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque()
        iq=deque()
        q.append(root)
        iq.append(0)
        w=1
        while q:
            l = len(q)
            
            for i in range(l):
                node=q.popleft()
                index=iq.popleft()
                if i==0:b=index
                if i==l-1:a=index

                if node.left:q.append(node.left);iq.append(index*2)
                if node.right:q.append(node.right);iq.append(index*2+1)
            w=max(w,a-b+1)
        return w

