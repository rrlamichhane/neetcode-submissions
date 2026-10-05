# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is a valid binary search tree (BST).
        
        This function uses a recursive depth-first search approach to validate
        the BST properties by checking if each node's value lies within the allowed
        bounds (lower and upper). The bounds are updated as we traverse down the tree.
        
        Args:
        root (Optional[TreeNode]): The root of the binary tree.
        
        Returns:
        bool: True if the tree is a valid BST, False otherwise.
        """
        
        def validate(node: Optional[TreeNode], lower: float, upper: float) -> bool:
            # If we reach a null node, it means we are valid up to this point
            if not node:
                return True
            # Check the current node's value is within the bounds
            if not (lower < node.val < upper):
                return False
            # Recursively validate the left and right subtrees with updated bounds
            return (validate(node.left, lower, node.val) and  # Left subtree must be less than current node
                    validate(node.right, node.val, upper))  # Right subtree must be greater than current node
            
        # Initiate validation with the entire range of possible values
        return validate(root, float('-inf'), float('inf'))