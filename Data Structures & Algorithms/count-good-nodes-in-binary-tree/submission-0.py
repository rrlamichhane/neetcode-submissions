# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, count, max_val):
            if not root:
                return count
            if root.val >= max_val:
                count += 1
            max_val = max(root.val, max_val)
            count = dfs(root.left, count, max_val)
            count = dfs(root.right, count, max_val)
            return count
        
        if not root:
            return 0
        
        return dfs(root, 0, root.val)
        