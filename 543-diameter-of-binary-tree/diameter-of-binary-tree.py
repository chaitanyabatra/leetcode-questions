# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.md=0
        def go(node):
            if not node:return -1
            l=go(node.left)
            r= go(node.right)
            self.md=max(self.md,l+2+r)
            return 1+max(l,r)
        go(root)
        return self.md
        