# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def go(node,p,q):
            if not node or node==p or node==q:
                return node
            l=go(node.left,p,q)
            r=go(node.right,p,q)
            if l and r:return node
            if not l:return r
            if not r:return l
        return go(root,p,q)

        