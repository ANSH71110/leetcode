# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        h=l1
        while l1 is not None or l2 is not None or carry==1:
            #print(h)
            if l1 is not None and l2 is not None:
                l1.val+=l2.val+carry
                carry=l1.val//10
                l1.val%=10
                l2=l2.next
                if l1.next is None:
                    c=l1
                l1=l1.next                          
            elif l2 is None and l1 is not None:
                if carry==1:
                    l1.val+=carry
                    carry=l1.val//10
                    l1.val%=10
                    if l1.next is None and carry==1:
                        t=ListNode(carry)
                        l1.next=t
                        carry=0
                l1=l1.next
            elif l1 is None:
                l1=c
                if l2 is None:
                    t=ListNode(carry)
                    l1.next=t
                    break
                t=ListNode(carry+l2.val)
                l1.next=t
                l1=l1.next
                c=l1
                carry=l1.val//10
                l1.val%=10
                l2=l2.next
                l1=l1.next
        return h
