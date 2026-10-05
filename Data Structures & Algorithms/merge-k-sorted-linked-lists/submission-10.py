from heapq import heappush, heappop
from typing import List, Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Use a min-heap to always extract the smallest current node among the k lists.
        Each pop adds one node to the answer and pushes that node's successor if it exists. O(n log k) time, O(k) space.
        """
        # First, let's prepare a heap with the head node from each non-empty list.
        min_heap: List[Tuple[int, int, ListNode]] = []

        # We need a unique tie-breaker because ListNode objects themselves are not directly comparable.
        unique_index = 0

        # Now we scan all input lists and seed the heap with their first node.
        for node in lists:
            # We only push real nodes; empty lists contribute nothing.
            if node is not None:
                heappush(min_heap, (node.val, unique_index, node))
                unique_index += 1

        # A dummy head makes it much simpler to build the merged list uniformly.
        dummy_head = ListNode()
        tail = dummy_head

        # While there is still at least one candidate node available, keep taking the smallest one.
        while min_heap:
            # The heap gives us the globally smallest current node across all lists.
            _, _, smallest_node = heappop(min_heap)

            # We attach that node directly to the result list.
            tail.next = smallest_node
            tail = tail.next

            # If the extracted node has a successor, that successor becomes this list's next candidate.
            if smallest_node.next is not None:
                heappush(min_heap, (smallest_node.next.val, unique_index, smallest_node.next))
                unique_index += 1

        # Finally, the merged list starts right after the dummy node.
        return dummy_head.next
