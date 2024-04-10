# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        maxw=1
        q=deque([root])
        iq=deque([1])
        while q:
            levelsize=len(q)
            l,r=0,0

            for i in range(levelsize):
                node=q.popleft()
                index=iq.popleft()

                if i==0:
                    l=index
                if i==levelsize-1:
                    r=index
                if node.left:
                    q.append(node.left)
                    iq.append(index*2)
                if node.right:
                    q.append(node.right)
                    iq.append(2*index+1)
            maxw=max(maxw,r-l+1)
        return maxw