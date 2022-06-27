# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        h=head
        n=0
        while h:
            n+=1
            h=h.next
        j=n//2
        h=head
        while j>0:
            h=h.next
            j-=1        
        curr=h
        nt=h
        h=None
        j=n//2
        while j>0:
            nt=nt.next
            curr.next=h
            h=curr
            curr=nt
            j-=1
        sum=0
        while head and h:
            sum=max(sum,head.val+h.val)
            head=head.next
            h=h.next
        return sum
