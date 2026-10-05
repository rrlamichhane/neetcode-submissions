# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_identical(n1, n2):
            if not n1 and not n2:
                return True
            if n1 and n2 and n1.val == n2.val:
                return is_identical(n1.left, n2.left) and is_identical(n1.right, n2.right)
            return False
        
        if not subRoot:
            return True
        if not root:
            return False
        if is_identical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        