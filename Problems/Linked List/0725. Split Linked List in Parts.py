# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        z=head
        n=0
        while z is not None:
            z=z.next
            n+=1
        l=[]
        z=head
        while k>0:
            j=0
            a=z
            while j<ceil(n/k)-1 and z is not None:
                z=z.next
                j+=1
            if z is None:
                i=0
                t=None
                while i<k:
                    l.append(t)
                    i+=1
                break
            t=z.next
            z.next=None
            l.append(a)
            z=t
            n-=ceil(n/k)
            k-=1
        return l
