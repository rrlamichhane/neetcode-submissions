# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            ans = list1
            list1 = list1.next
        else:
            ans = list2
            list2 = list2.next
        
        root = ans
        
        while list1 and list2:
            if list1.val <= list2.val:
                ans.next = list1
                list1 = list1.next
            else:
                ans.next = list2
                list2 = list2.next
            ans = ans.next
        
        if list1:
            ans.next = list1
        if list2:
            ans.next = list2
        
        return root
        