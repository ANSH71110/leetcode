# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        tag=0
        if head:
            while slow and fast and fast.next:
                slow=slow.next
                fast=fast.next.next
                if slow is fast:
                    tag=1
                    break
            
            fast=head
            while tag==1:
                if fast is slow:
                    print(fast.val)
                    return fast
                fast=fast.next
                slow=slow.next
        return None
