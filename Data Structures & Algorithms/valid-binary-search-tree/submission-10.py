# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recur_is_valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return recur_is_valid(node.left, left, node.val) and recur_is_valid(node.right, node.val, right)
        
        return recur_is_valid(root, float("-inf"), float("+inf"))
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        q = collections.deque([(root, float("-inf"), float("+inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))
        
        return True
