# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = root.val

        def dfs(root):
            nonlocal result
            if not root:
                return 0
            sl = max(0, dfs(root.left))
            sr = max(0, dfs(root.right))
            result = max(result, root.val + sl + sr)
            return root.val + max(sl, sr)
        
        dfs(root)
        return result

            

    def maxPathSum_ranjan(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float("-infinity")
        ans = root.val
        sl = self.maxPathSum(root.left)
        sr = self.maxPathSum(root.right)
        ans = max(sl+sr+ans, sl+ans, sr+ans, ans, sl, sr)
        print(root.val, sl, sr, ans)
        return ans
        