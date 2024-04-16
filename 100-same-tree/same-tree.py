# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def go(np,nq):
            if not np and not nq:return True
            if not np or not nq:return False
            return np.val==nq.val and go(np.left,nq.left) and go(np.right,nq.right)
        return go(p,q)
        