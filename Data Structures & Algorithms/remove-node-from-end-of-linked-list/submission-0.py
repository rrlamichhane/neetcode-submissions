# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        while slow:
            print(slow.val)
            fast = slow.next
            for _ in range(n):
                if not fast:
                    return head.next
                fast = fast.next
            if not fast:
                slow.next = slow.next.next
                break
            slow = slow.next
        return head
