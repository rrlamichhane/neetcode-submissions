# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = root.val

        def dfs_smallest(node):
            nonlocal res, count
            if not node:
                return
            dfs_smallest(node.left)
            count -= 1
            if count == 0:
                res = node.val
                return 
            dfs_smallest(node.right)
        
        dfs_smallest(root)
        return res
        