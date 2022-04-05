# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        else:
            if list1.val<list2.val:
                list3=head=ListNode(list1.val)
                list1=list1.next
            else:
                list3=head=ListNode(list2.val)
                list2=list2.next
            
            while list1 is not None or list2 is not None:
                if list1 is None:
                    list3.next=ListNode(list2.val)
                    list3=list3.next
                    list2=list2.next

                elif list2 is None:
                    list3.next=ListNode(list1.val)
                    list3=list3.next           
                    list1=list1.next
                else:
                    if list1.val<list2.val:
                        list3.next=ListNode(list1.val)
                        list3=list3.next
                        list1=list1.next
                    else:
                        list3.next=ListNode(list2.val)
                        list3=list3.next
                        list2=list2.next                    
            return head                    
