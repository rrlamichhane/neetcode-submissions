"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp_head = head
        node_map = {None: None}
        i = 0
        while temp_head:
            node_map[temp_head] = Node(temp_head.val)
            temp_head = temp_head.next
        temp_head = head
        while temp_head:
            node = node_map[temp_head]
            node.random = node_map[temp_head.random]
            temp_head = temp_head.next
            node.next =node_map[temp_head]
        return node_map[head]
        
        