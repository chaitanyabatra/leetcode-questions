"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q=[(root,0)]
        previnlevel={}

        while q:
            n,l=q.pop(0)
            if l in previnlevel:
                previnlevel[l].next=n
            if n.left:
                q.append((n.left,l+1))
            if n.right:
                q.append((n.right,l+1))
            previnlevel[l]=n
        return root
