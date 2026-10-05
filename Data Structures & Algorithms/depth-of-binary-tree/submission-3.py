# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recur_depth(cur_depth, root):
            if not root:
                return cur_depth
            
            cur_depth += 1
            cur_depth = max(recur_depth(cur_depth, root.left), cur_depth, recur_depth(cur_depth, root.right))
            return cur_depth
        
        return recur_depth(0, root)
        