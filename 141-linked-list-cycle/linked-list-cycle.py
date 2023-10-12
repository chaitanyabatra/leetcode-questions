# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# using tortoise and hare algorythm, traversing one pointer twice as fast as the other, and then if they meet, there exists a linked list cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise=head
        rabbit=head

        while rabbit and rabbit.next and rabbit.next.next:
            tortoise=tortoise.next
            rabbit=rabbit.next.next

            if rabbit==tortoise:
                return True
        return False