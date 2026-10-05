# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        stack = []
        forward_head = dummy_head = head
        while dummy_head:
            stack.append(dummy_head)
            dummy_head = dummy_head.next
        print(stack)
        tmp_head = None
        list_len = len(stack)
        i = 0
        while head:
            print(i, len(stack), head.val)
            if i == list_len - 1:
                head.next = None
                break
            if i%2 == 0:
                tmp_head = head.next
                head.next = stack.pop()
                head.next.next = tmp_head
            head = head.next
            i += 1

        return None
        