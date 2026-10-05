# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def recur_reorder(root: Optional[ListNode], node: Optional[ListNode]) -> None:
            if not node: 
                return root
            root = recur_reorder(root, node.next)

            if not root:
                return None
            tmp = None
            if root == node or root.next == node:
                node.next = None
            else:
                tmp = root.next
                root.next = node
                node.next = tmp
            return tmp
        
        recur_reorder(head, head.next)

            


    def reorderList_linear(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        stack = []
        forward_head = dummy_head = head
        while dummy_head:
            stack.append(dummy_head)
            dummy_head = dummy_head.next
        tmp_head = None
        list_len = len(stack)
        i = 0
        while head:
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
        