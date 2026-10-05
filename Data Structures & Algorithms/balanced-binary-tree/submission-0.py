# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recur_height(self, root, h):
        if h < 0 or not root:
            return h
        lh = self.recur_height(root.left, h+1)
        rh = self.recur_height(root.right, h+1)
        if abs(lh - rh) > 1:
            return -1
        return max(lh, rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return False if self.recur_height(root, 1) < 0 else True
        