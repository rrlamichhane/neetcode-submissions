# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([[root]])
        right_view = []

        while q:
            nodes = q.popleft()
            right_view.append(nodes[-1].val)
            children = []
            for n in nodes:
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)
            q.append(children) if children else None
        
        return right_view
