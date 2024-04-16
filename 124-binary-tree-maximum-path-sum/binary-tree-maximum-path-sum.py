# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ms=-inf
        def go(node):
            nonlocal ms
            if not node:
                return 0
            l=go(node.left)
            r=go(node.right)
            if l<0:l=0
            if r<0:r=0
            ms=max(ms,l+r+node.val)
            return max(l,r)+node.val
        go(root)
        return ms
        