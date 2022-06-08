# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=0
        a=ListNode()
        b=ListNode()
        z=head
        a1=a
        b1=b
        while z is not None:
            #print(a1,b1,a,b,i)
            if i%2==0:                
                a.next=ListNode(z.val)
                a=a.next
            else:             
                b.next=ListNode(z.val)
                b=b.next
            z=z.next
            i+=1
        head=a1.next
        a.next=b1.next
        return head
