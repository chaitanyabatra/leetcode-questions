# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        adder=[]
        while curr.next:
            curr.val=curr.val*2
            adder.append(curr.val//10)
            curr.val%=10
            curr=curr.next
        curr.val=curr.val*2
        adder.append(curr.val//10)
        curr.val%=10
        curr=head
        if adder[0]!=0:
            a=ListNode(adder[0],head)
            head=a
        i=1
        while curr.next:
            curr.val+=adder[i]
            i+=1
            curr=curr.next
        return head