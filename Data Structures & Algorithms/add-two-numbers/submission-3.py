# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = node = ListNode()
        while l1 or l2:
            if l1 and l2:
                cur_sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                cur_sum = l1.val + carry
                l1 = l1.next
            else:
                cur_sum = l2.val + carry
                l2 = l2.next
            carry = 0
            if cur_sum >= 10:
                carry = 1
                cur_sum = cur_sum % 10
            node.val = cur_sum
            if l1 or l2:
                node.next = ListNode()
                node = node.next
        if carry > 0:
            node.next = ListNode(carry)
        return res
        