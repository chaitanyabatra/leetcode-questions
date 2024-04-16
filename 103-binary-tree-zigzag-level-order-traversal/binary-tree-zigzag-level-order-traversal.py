# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        use stack and deque for bfs
        """
        ans=[]
        if not root:
            return []
        revers=False
        q=deque()
        q.append(root)
        while q:
            l=len(q)
            level=[]
            for i in range(l):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if revers:
                level=level[::-1]
            revers= not revers
            ans.append(level)
        return ans