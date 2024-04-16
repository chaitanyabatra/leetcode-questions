# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l=root.left
        r=root.right
        def go(l,r):
            if not l or not r:
                return l==r
            return go(l.right,r.left) and go(l.left,r.right) and l.val==r.val
        return go(l,r)