# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return root
        def f(node):
            if not node: return node
            if node.val==val:return node
            if node.val>val: return f(node.left)
            else : return f(node.right) 
        return f(root)