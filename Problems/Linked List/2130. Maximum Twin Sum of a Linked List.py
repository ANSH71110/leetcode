# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        i=0
        sum=0
        j=len(arr)-1
        while i<j:
            if i!=j:
                sum=max(sum,arr[i]+arr[j])
                arr.pop
            i+=1
            j-=1
        return sum
