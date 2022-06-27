# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        nt=head
        prev=None
        while curr:
            nt=nt.next
            curr.next=prev
            prev=curr
            curr=nt
        return prev
