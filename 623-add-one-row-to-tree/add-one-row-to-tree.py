# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            node=TreeNode(val)
            node.left=root
            root=node
        q=deque()
        q.append(root)
        depth-=2
        while q and depth:
            l=len(q)
            for i in range(l):
                node=q.popleft()
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            depth-=1
        while q:
            node=q.popleft()
            if True:
                tempnode=TreeNode(val)
                tempnode.left=node.left
                node.left=tempnode
            if True:
                tempnode=TreeNode(val)
                tempnode.right=node.right
                node.right=tempnode
        return root