# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=1
        h=head
        l1=[]
        tag=1
        while h:
            j=0
            l=[]
            while j<i and h:                
                l.append(h.val)
                if h.next is None:
                    tag=0
                    break
                h=h.next
                j+=1
            if len(l)%2==0:
                l=l[::-1]
            l1.extend(l)
            i+=1
            if tag==0:
                break
        i=0
        h=head
        while i<len(l1):
            h.val=l1[i]
            h=h.next
            i+=1
        return head
