# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth_recur(self, depth: int, root: Optional[TreeNode]) -> int:
        left_depth = right_depth = depth
        if not root:
            return depth
        if root.left:
            left_depth = self.depth_recur(depth+1, root.left)
        if root.right:
            right_depth = self.depth_recur(depth+1, root.right)
        return max(left_depth, right_depth)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        