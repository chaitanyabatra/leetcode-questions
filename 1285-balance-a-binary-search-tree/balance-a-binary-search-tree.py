# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_traversal(self, root):
        arr = []
        def inorder(node):
            if node:
                inorder(node.left)
                arr.append(node.val)
                inorder(node.right)
        inorder(root)
        return arr
    
    def build_new(self, arr):
        left, right = 0, len(arr)
        if left == right:
            return None
        else:
            mid = (left + right)//2
            node = TreeNode(arr[mid])
            node.left = self.build_new(arr[:mid])
            node.right = self.build_new(arr[mid+1:])
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = self.inorder_traversal(root)
        ret = self.build_new(arr)
        return ret

        