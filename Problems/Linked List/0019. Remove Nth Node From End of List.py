# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=1
        len=0
        z=head
        while z is not None:
            len+=1
            z=z.next
        if len==n:
            return head.next
        len-=n
        z=head
        while i<len:
            z=z.next
            i+=1
        print(z)
        t=z.next
        z.next=t.next
        return head
