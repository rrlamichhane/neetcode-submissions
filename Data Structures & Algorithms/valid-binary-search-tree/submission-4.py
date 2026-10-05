# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_dfs(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return is_valid_dfs(node.left, left, node.val) and is_valid_dfs(node.right, node.val, right)
        return is_valid_dfs(root, float("-inf"), float("+inf"))

    def isValidBST_ranjan(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = root.left.val if root.left else float("-inf")
        right = root.right.val if root.right else float("+inf")
        if not (left < root.val < right):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)