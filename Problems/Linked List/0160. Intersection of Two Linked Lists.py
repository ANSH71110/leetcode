# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        i=1
        z1=headA
        while z1.next is not None:
            z1=z1.next
            i+=1
        j=1
        z2=headB
        while z2.next is not None:
            z2=z2.next
            j+=1
        if z1==z2:
            k=0
            if i<j:
                d=j-i                
                while k<d:
                    headB=headB.next
                    k+=1
            else:
                d=i-j               
                while k<d:
                    headA=headA.next
                    k+=1
            while headA and headB:
                if headA is headB:
                    return headA
                headA=headA.next
                headB=headB.next
        else:
            return None
