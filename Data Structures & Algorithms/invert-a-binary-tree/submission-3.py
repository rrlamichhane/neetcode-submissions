# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        dummy = root
        def recur_invert(root):
            if not root:
                return None
            root.left, root.right = root.right, root.left
            recur_invert(root.left)
            recur_invert(root.right)
        
        recur_invert(root)

        return dummy


        