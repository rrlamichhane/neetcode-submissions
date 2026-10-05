"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs_copy(node):
            if node in old_to_new:
                return old_to_new[node]
            
            node_copy = Node(node.val)
            old_to_new[node] = node_copy
            for nei in node.neighbors:
                node_copy.neighbors.append(dfs_copy(nei))
            return node_copy
        
        return dfs_copy(node) if node else None
