# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i=1
        arr=[]
        a=head
        while a:
            if i>=left and i<=right:
                arr.append(a.val)
            i+=1
            a=a.next
        i=1
        a=head
        while a:
            if i>=left and i<=right:
                a.val=arr.pop()
            i+=1
            a=a.next
        return head
