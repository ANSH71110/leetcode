# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        if head:
            slow=slow.next
            fast=fast.next
            while slow and fast and fast.next:
                slow=slow.next
                fast=fast.next
                fast=fast.next
                if slow is fast:
                    return 1
        return 0
