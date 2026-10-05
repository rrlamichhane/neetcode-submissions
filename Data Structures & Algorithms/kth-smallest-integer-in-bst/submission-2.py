# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            nonlocal arr
            if not node:
                return
            dfs(node.left)
            if len(arr) < k:
                arr.append(node.val)
            else:
                return
            dfs(node.right)
        
        dfs(root)

        return arr[-1] if arr else None
        