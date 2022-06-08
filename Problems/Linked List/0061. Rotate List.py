# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        z=head
        while z is not None:
            n+=1
            z=z.next
        if k==0 or n<=1 or k%n==0:
            return head
        k%=n
        i=0
        z=head
        while i<n-k-1:
            z=z.next
            i+=1
        t=z.next
        z.next=None
        z=t
        while t.next is not None:
            t=t.next
        t.next=head
        return z
