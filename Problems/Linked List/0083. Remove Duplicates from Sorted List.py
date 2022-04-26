# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h=head
        while h:
            if h.next and h.val == h.next.val:
                h.next=h.next.next
            else:
                h=h.next
        
        return head
